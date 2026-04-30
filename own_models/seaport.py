from hub import Hub
from enum import Enum
from typing import Self
import pyvisgraph as vg

class SeaportType(Enum):
    BASE = 1
    TERMINAL = 2
    PRIVATE = 3

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

    _graph = None

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

    def distance_to(self, other: Self):
        if Seaport._graph is None:
            raise RuntimeError("Maritime graph not initialized")
        return Seaport.maritime_distance(self.lon, self.lat, other.lon, other.lat, Seaport._graph)

    @classmethod
    def set_graph(cls, graph):
        cls._graph = graph
    
    @classmethod
    def maritime_distance(lon1: float, lat1: float, lon2: float, lat2: float, graph: vg.VisGraph) -> float:
        origin = vg.Point(lon1, lat1)
        destination = vg.Point(lon2, lat2)
        shortest = graph.shortest_path(
            graph.closest_point(origin, graph.point_in_polygon(origin)), 
            graph.closest_point(destination, graph.point_in_polygon(destination))
        )

        distances = [super().haversine_m(shortest[i][0], shortest[i][1], shortest[i+1][0], shortest[i+1][1]) for i in range(len(shortest) - 1)]
        return sum(distances)

    def __repr__(self):
        return (
            f"Seaport name: {self.name}\n"
            f"Seaport UN/LOCODE: {self.un_locode}\t Seaport PMO: {self.pmo}\n"
            f"Seaport coordinates: {self.geometry.coords[0]}\n"
            f"Seaport attraction: {self.attraction}"
        )