import sys
import os
from pathlib import Path

dir_models = Path().resolve() / "models"
sys.path.append(os.path.abspath(dir_models))

from building import Building
from parcel import Parcel
from road import Road
from household import Household

# Test for Parcel and SpatialObject
parcel1_data = {
    "parcel_id": "P1",
    "geometry": {
        "x": 121.055,
        "y": 12.11,
    },
    "area": 109.5,
    "zone": "Residential"
}

parcel2_data = {
    "parcel_id": "P2",
    "geometry": {
        "x": 121.06,
        "y": 12.11,
    },
    "area": 57.5,
    "zone": "Residential"
}

parcel1 = Parcel(**parcel1_data)
parcel2 = Parcel(**parcel2_data)

# print(parcel1.distance_to(parcel2))
# print(parcel1.intersects(parcel2, threshold=0.5))
# print(parcel1.compute_area())

# Test for Road

road1_data = {
    "road_id": "R2",
    "geometry": {
        "x": 121.07,
        "y": 12.10,
    },
    "length": 25.4,
    "road_type": "Tertiary"
}

road2_data = {
    "road_id": "R1",
    "geometry": {
        "x": 121.08,
        "y": 12.09,
    },
    "length": 37.3,
    "road_type": "Secondary"
}

road1 = Road(**road1_data)
road2 = Road(**road2_data)

road1.add_adjacent_parcel(parcel1)
road1.add_adjacent_parcel(parcel2)
road2.add_adjacent_parcel(parcel1)

print(parcel1.adjacent_roads)
print(road1.adjacent_parcels)
print(parcel1)