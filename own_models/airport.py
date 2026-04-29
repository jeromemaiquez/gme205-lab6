from hub import Hub
from enum import Enum
import math

class Airport(Hub):
    """
    Child class of Hub specifically to model airports.
    Has airport-specific attributes and calculates 
    distance via the Haversine distance method.

    Additional attributes:
    - iata_code: str
        The unique IATA code for the airport
    - airport_class: enum
        The airport's class (international, principal I and II, community)
    - num_runways: int
        No. of runways in the airport, as a proxy for capacity
    """

    def __init__(
        self, 
        name: str, 
        lon: float, 
        lat: float, 
        iata_code: str,
        icao_code: str,
        airport_type: AirportType,
        num_runways: int = None,
        attraction: float | None = None,
    ):
        super().__init__(name, lon, lat, attraction)
        self.iata_code = iata_code
        self.icao_code = icao_code
        self.airport_type = airport_type
        self.num_runways = num_runways

    def distance_to(self, other: Airport):
        """
        Computes the great-circle distance between two Airports
        using the Haversine distance method.
        """
        return Airport.haversine_m(self.lon, self.lat, other.lon, other.lat)

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

class AirportType(Enum):
    INTERNATIONAL = 1
    PRINCIPAL_1 = 2
    PRINCIPAL_2 = 3
    COMMUNITY = 4