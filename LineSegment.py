# Author: Dominic Fantauzzo
# GitHub username: fantauzd
# Date: 8/9/2023
# Description: Creates a class of Point and LineSegment objects
# that can be used to represent points and straight lines on an x,y coordinate plane.
# Includes functions for finding the distance between points, length and slope of line segments,
# and if two line segments are parallel


class Point:
    """
    represents a point on a cartesian plane with x and y-coordinates
    """

    # initializes the x and y_coordinates for the Point object
    def __init__(self, x_coordinate, y_coordinate):
        self._x_coord = x_coordinate
        self._y_coord = y_coordinate

    def get_x_coord(self):
        """
        returns the x-coordinate of the Point
        """
        return self._x_coord

    def get_y_coord(self):
        """
        returns the y_coordinate of the Point
        """
        return self._y_coord

    def distance_to(self, p_object):
        """
        finds and returns the distance between the Point object the method is called on
        and the Point object passed as the argument
        """
        # finds the distance between the two points using formula provided
        x = ((p_object.get_x_coord() - self._x_coord) ** 2)
        y = ((p_object.get_y_coord() - self._y_coord) ** 2)
        return (x+y)**0.5


class LineSegment:
    """
    represents a straight line segment with two endpoints
    """

    # initializes the endpoints for the LineSegment object
    def __init__(self, ep_1, ep_2):
        self._endpoint_1 = ep_1
        self._endpoint_2 = ep_2

    def get_endpoint_1(self):
        """
        returns the first endpoint of the LineSegment
        """
        return self._endpoint_1

    def get_endpoint_2(self):
        """
        returns the second endpoint of the LineSegment
        """
        return self._endpoint_2

    def length(self):
        """
        takes no arguments and returns the distance between the LineSegment's two endpoints
        """
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """
        takes no arguments and returns the slope of the LineSegment
        """
        rise = (self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord())  # finds the rise of the two points
        run = (self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord())  # finds the run of the two points
        return rise / run  # finds and returns the slope

    def is_parallel_to(self, ls_object):
        """
        takes a LineSegment object as an argument. It returns True if the LineSegment
        the method is being called on is parallel to the one being passed as the argument
        """
        # checks if the slope of the two line segments are significantly different and returns True if they are not
        if (abs(self.slope() - ls_object.slope())) < 0.0000001:
            return True
        else:
            return False
