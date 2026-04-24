from spatial_object import SpatialObject

class Road(SpatialObject):
    """
    Road is a spatial object with the following attributes:
    - geometry
    - length
    - type

    Relationship:
    - adjacent to one or more parcels
    """

    def __init__(self, road_id: str, geometry: dict, length: float, road_type: str):
        super().__init__(geometry)
        self.road_id = road_id
        self.length = length
        self.road_type = road_type
        self.adjacent_parcels = []

    def get_length(self):
        return self.length
    
    def add_adjacent_parcel(self, parcel):
        if parcel not in self.adjacent_parcels:
            parcel.add_adjacent_road(self)
            self.adjacent_parcels.append(parcel)
    
    def describe(self):
        parcel_ids = [p.parcel_id for p in self.adjacent_parcels]
        return (
            f"Road {self.road_id}: type={self.road_type}, "
            f"length={self.length}, adjacent_parcels={parcel_ids}"
        )
    
    def __repr__(self):
        return f"{self.road_id}"