from shapely import Point, Polygon
from pathlib import Path
import math

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
    
    @staticmethod
    def haversine_m(lon1: float, lat1: float, lon2: float, lat2: float) -> float:
        """
        Compute the Haversine distance between two lon/lat pairs in meters.
        """
        R = 6_371_000.0

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = (
            math.sin(dphi / 2) ** 2
            + math.cos(phi1)
            * math.cos(phi2)
            * math.sin(dlambda / 2) ** 2
        )

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def __repr__(self):
        return (
            f"Hub name: {self.name}\n"
            f"Hub coordinates: {self.geometry.coords[0]}\n"
            f"Hub attraction: {self.attraction}"
        )
    
