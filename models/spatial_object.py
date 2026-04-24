from math import sqrt

class SpatialObject:
    """
    Base class for spatial objects.
    Geometry is simplified as a dictionary  with x and y coordinates.

    Example:
        geometry = {"x": 10, "y": 20}
    """

    def __init__(self, geometry: dict):
        self.geometry = geometry

    def distance_to(self, other):
        """
        Compute Euclidean distance between this object and another spatial object.
        """
        x1 = self.geometry["x"]
        y1 = self.geometry["y"]
        x2 = other.geometry["x"]
        y2 = other.geometry["y"]

        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    def intersects(self, other: SpatialObject, threshold=0.0):
        """
        Simplified intersection logic:
        treat intersection as occupying the same coordinate,
        or within a threshold distance if provided.
        """
        return self.distance_to(other) <= threshold