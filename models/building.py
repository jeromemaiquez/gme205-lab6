from spatial_object import SpatialObject

class Building(SpatialObject):
    """
    Building is a spatial object with the following attributes:
    - geometry
    - height
    - usage

    Relationship:
    - located on one parcel
    - may contain multiple households
    """

    def __init__(self, building_id: str, geometry: dict, height: float, usage: str, parcel=None):
        super().__init__(geometry)
        self.building_id = building_id
        self.height = height
        self.usage = usage
        self.parcel = parcel
        self.households = []

        if self.parcel is not None:
            self.parcel.add_building(self)
        
    def get_height(self):
        return self.height
    
    def assign_parcel(self, parcel):
        self.parcel = parcel
        self.parcel.add_building(self)

    def add_household(self, household):
        if household not in self.households:
            self.households.append(household)
    
    def describe(self):
        parcel_text = self.parcel.parcel_id if self.parcel else "None"
        return (
            f"Building {self.building_id}: usage={self.usage}, "
            f"height={self.height}, parcel={parcel_text}, "
            f"households={len(self.households)}" 
        )
    
    def __repr__(self):
        return f"{self.building_id}"