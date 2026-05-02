import openrouteservice as ors
from hub import Hub
import geopandas as gpd
import pandas as pd
from tqdm import tqdm
import time

def draw_isochrones(
        client: ors.Client, 
        hubs: list[Hub], 
        hub_id: str,
        travel_range: int = 3_600,
        get_pop: bool = True,
) -> gpd.GeoDataFrame:
    """
    Returns a geopandas.GeoDataFrame of isochrone polygons
    for a list of Hub objcts via the OpenRouteService API

    Attributes:
    - client: ors.Client
        Client object supplied with the API key
    - hubs: list[Hub]
        List of Hub objects for which to create isochrones
    - travel_range: int
        Ranges to calculate travel duration for (in seconds)
    - get_pop: bool
        If True, calculates total population inside isochrone.
        Population data from GHSL by the EU JRC
    """
    all_isochrones = []

    for i in tqdm(range(0, len(hubs), 5)):
        try:
            chunk_hubs = hubs[i:i+5]
        except IndexError:  # If len(chunk_hubs) < 5
            chunk_hubs = hubs[i:]
        
        locations = [hub.coords[::-1] for hub in chunk_hubs]
        
        attributes = None
        if get_pop:
            attributes = ["total_pop"]

        chunk_isochrones = ors.isochrones.isochrones(
            client=client,
            locations=locations,
            range=[travel_range],
            attributes=attributes
        )

        gdf_chunk = gpd.GeoDataFrame.from_features(chunk_isochrones)

        all_isochrones.append(gdf_chunk)

        time.sleep(5)
        # break

    # print(chunk_isochrones)
    
    df_isochrones = pd.concat(all_isochrones, ignore_index=True)
    gdf_isochrones = gpd.GeoDataFrame(data=df_isochrones, geometry=df_isochrones.geometry, crs="EPSG:4326")
    gdf_isochrones["hub_id"] = gdf_isochrones.index.to_series().apply(
       lambda idx: getattr(hubs[idx], hub_id)
    )

    return gdf_isochrones