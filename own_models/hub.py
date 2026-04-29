from shapely import Point, Polygon
from pathlib import Path

class Hub:
    """
    Base class for transport hubs (airport and seaport),
    which are modeled as point locations.

    Attributes:
    - name: str
        Name of the transport hub
    - lon: float
        Longitude of the transport hub
    - lat: float
        Latitude of the transport hub
    - attraction: int/float
        Attraction/size score of the transport hub
    """

    def __init__(self, name: str, lon: float, lat: float, attraction: float | None = None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180") 
        if not (-90 <= lat <= 180):
            raise ValueError("Latitude must be between -90 and 90")
        
        self.lon = lon
        self.lat = lat
        self.geometry = Point(lon, lat)
        self.name = name
        self.attraction = attraction

    def set_attraction(self, value: int | float, override: bool = False) -> None:
        """
        Assigns a value as a score signifying "attraction"
        or "size" of a given hub in the radiation model.

        Attributes:
        - value: int or float
            Value to assign as the hub's attraction/size score
        - override: bool
            If True, overrides any existing attraction score
        """
        if (self.attraction) & (not override):
            raise ValueError("Hub already has an attraction score. Set `override=True` if you wish to override")
        
        self.attraction = value
    
    def distance_to(self, other) -> float:
        raise NotImplementedError("Must be implemented by Airport or Seaport subclass")
    
    def __repr__(self):
        return (
            f"Hub name: {self.name}\n"
            f"Hub coordinates: {self.geometry.coords}"
            f"Hub attraction: {self.attraction}"
        )
    
