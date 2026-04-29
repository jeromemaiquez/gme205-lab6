from hub import Hub
from enum import Enum
import pyvisgraph as vg

class Seaport(Hub):
    """
    Child class of Hub specifically to model seaports.
    Has seaport-specific attributes and calculates distance
    via visibility graphs (using the pyvisgraph package).

    Additional attributes:
    - un_locode: str
        The unique UN/LOCODE code for the seaport
    - pmo: str
        The port management office (PMO) overseeing the seaport
    - seaport_type: enum
        The seaport classification (base, terminal, private)
    - num_berths: int
        No. of berths in the seaport, as a proxy for capacity
    """

    def __init__(
        self, 
        name: str, 
        lon: float, 
        lat: float, 
        un_locode: str,
        pmo: str,
        seaport_type: SeaportType,
        num_berths: int = None,
        attraction: float | None = None,
    ):
        super().__init__(name, lon, lat, attraction)
        self.un_locode = un_locode
        self.pmo = pmo
        self.seaport_type = seaport_type
        self.num_berths = num_berths

class SeaportType(Enum):
    BASE = 1
    TERMINAL = 2
    PRIVATE = 3