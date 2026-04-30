import sys
import os
import pyvisgraph as vg
from pathlib import Path

dir_models = Path().resolve() / "own_models"
sys.path.append(os.path.abspath(dir_models))
fp_graph = Path().resolve() / "own_data" / "PH_SeaRouteGraph.pk1"

from airport import Airport, AirportType
from seaport import Seaport, SeaportType

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

print("\nAirport 2 details:\n---", airport2, sep="\n")
print(f"Distance between airports 1 and 2: {airport1.distance_to(airport2)} m")
print(f"Route coordinates between airports 1 and 2: {airport1.route_coords(airport2)}")
print(f"Geometry of route between airports 1 and 2: {airport1.route_linestring(airport2)}")

# Test for Seaport

# Import existing VisGraph for sea routes & assign to Seaport class
# VisGraph was pre-made due to long build times (~35 minutes)
# searoute_graph = vg.VisGraph()
# searoute_graph.load(fp_graph)
# Seaport.set_graph(searoute_graph)

# seaport1_data = {
#     "name": "Port of Manila",
#     "lon": 120.9500,
#     "lat": 14.5833,
#     "un_locode": "PHMNL",
#     "pmo": "NCR",
#     "seaport_type": SeaportType.BASE
# }

# seaport2_data = {
#     "name": "Port of Cagayan de Oro",
#     "lon": 124.6623,
#     "lat": 8.4939,
#     "un_locode": "PHCDO",
#     "pmo": "MO/C",
#     "seaport_type": SeaportType.BASE
# }

# seaport1 = Seaport(**seaport1_data)
# seaport2 = Seaport(**seaport2_data)

# print("\nSeaport 2 details:\n---", seaport2, sep="\n")
# print(f"Distance between seaports 1 and 2: {seaport1.distance_to(seaport2)} m")