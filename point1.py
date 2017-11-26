"""This is Chapter 15: Classes and Objects

Learning Python programming using the book titled

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2017 Daniel Emaasit

License: http://creativecommons.org/licenses/by/4.0/
"""
from numpy import sqrt
from copy import deepcopy

class Point:                               # the header defines the class
    """Represents a point in 2-D space.     
    
    attributes: x, y.
    """                                   # this docstring explains what this class is for
    
    def __init__(self, x = 0, y = 0)
    """Initializes a Point object
    
    Parameters
    ----------
    
    x : float
    y : float
    
    Returns
    -------
    a Point object
    """
    self.x = x
    self.y = y
    
    def print_point(p):
        """Print a Point object"""
        print((p.x, p.y))

    def distance_between_points(p1, p2):
        """Computes the distance between two points.

        p1: Point
        p2: Point

        returns: float 
        """
        x_diff = (p1.x - p2.x)**2
        y_diff = (p1.y - p2.y)**2
        dist = sqrt(x_diff + y_diff)
        return dist  

    class Rectangle:
        """Represents a rectangle.

        attributes: width, length, corner.
        """
    def find_center(rect):                              # a function that returns an instance
        """Returns a Point at the center of a Rectangle

        attributes: Rectangle

        returns: new Point
        """
        p = Point()
        p.x = rect.corner.x + rect.width/2
        p.y = rect.corner.y + rect.height/2
        return p    

    def grow_rectangle(rect, dwidth, dheight):
        """Modifies a Rectangle by adding to its width and height

        attributes: rect, dwidth, dheight.

        rect: Rectangle object
        dwidth: change in width
        dheight: change in height
        """
        rect.width += dwidth
        rect.height += dheight

    def move_rectangle(rect, dx, dy):
        """Modifies the corner of a Rectangle by adding to its x & y coordinates

        attributes: rect, dx, dy.

        rect: Rectangle object
        dx: change in x coordinate
        dy: change in y coordinate
        """
        rect.corner.x += dx
        rect.corner.y += dy

    def move_rectangle_copy(rect, dx, dy):
        """Modifies the corner of a Rectangle by adding to its x & y coordinates

        attributes: rect, dx, dy.

        rect: Rectangle object
        dx: change in x coordinate
        dy: change in y coordinate
        """    
        new_rect = deepcopy(rect)
        move_rectangle(new_rect, dx, dy)
        return new_rect

def main():
    # this is main
    blank = Point()
    
    box = Rectangle()
    box.width = 100
    box.height = 200
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0
    
if __name__ == "__main__":
    main()