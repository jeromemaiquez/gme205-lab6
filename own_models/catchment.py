import openrouteservice as ors
from hub import Hub
import pandas as pd
import geopandas as gpd

def draw_isochrones(
        client: ors.Client, 
        hubs: list[Hub], 
        hub_id: str,
        travel_range: int = 7_200,
        get_pop: bool = True
) -> gpd.GeoDataFrame:
    """
    Returns a geopandas.GeoDataFrame of isochrone polygons
    for a list of Hub objcts via the OpenRouteService API

    Attributes:
    - client: ors.Client
        Client object supplied with the API key
    - hubs: list[Hub]
        List of Hub objects for which to create isochrones
    - range: int
        Ranges to calculate travel duration for (in seconds)
    - get_pop: bool
        If True, calculates total population inside isochrone.
        Population data from GHSL by the EU JRC
    """
    all_isochrones = []

    for i in range(0, len(hubs), step=5):
        try:
            chunk_hubs = hubs[i:i+5]
        except IndexError:  # If len(chunk_hubs) < 5
            chunk_hubs = hubs[i:]
        
        locations = [hub.coords[::-1] for hub in chunk_hubs]
        
        attributes = None
        if get_pop:
            attributes = ["total_pop"]

        all_isochrones += ors.isochrones.isochrones(
            client=client,
            locations=locations,
            range=travel_range,
            attributes=attributes
        )
    
    gdf_isochrones = gpd.GeoDataFrame.from_features(all_isochrones).set_crs("EPSG:4326")
    gdf_isochrones["hub_id"] = gdf_isochrones.index.to_series().apply(
       lambda idx: getattr(hubs[idx], hub_id)
    )

    return gdf_isochrones