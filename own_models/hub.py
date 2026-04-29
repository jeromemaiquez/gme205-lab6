from shapely import Point, Polygon

class Hub:
    """
    Base class for transport hubs (airport and seaport).
    Contains ability to draw catchment (via ORS API isochrone)
    and aggregate some variable as its size/"attraction".

    Attributes:
    - name: str
    - lon: longitude (x-coordinate)
    - lat: latitude (y-coordinate)
    - catchment: shapely.Polygon (default: None)
    """

    def __init__(self, hub_name: str, lon: float, lat: float, catchment: Polygon | None = None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180") 
        if not (-90 <= lat <= 180):
            raise ValueError("Latitude must be between -90 and 90")
        
        self.lon = lon
        self.lat = lat
        self.geometry = Point(lon, lat)
        self.hub_name = hub_name
        self.catchment = catchment

    
