import sys
import os
from pathlib import Path

dir_models = Path().resolve() / "own_models"
sys.path.append(os.path.abspath(dir_models))

from airport import Airport, AirportType

# Test for Airport
airport1_data = {
    "name": "Ninoy Aquino International Airport",
    "lon": 121.0165,
    "lat": 14.5123,
    "iata_code": "MNL",
    "icao_code": "RPLL",
    "airport_type": AirportType.INTERNATIONAL
}

airport2_data = {
    "name": "Mactan-Cebu International Airport",
    "lon": 123.9790,
    "lat": 10.3075,
    "iata_code": "CEB",
    "icao_code": "RPVM",
    "airport_type": AirportType.INTERNATIONAL
}

airport1 = Airport(**airport1_data)
airport2 = Airport(**airport2_data)

print(airport2)
print(airport1.distance_to(airport2))