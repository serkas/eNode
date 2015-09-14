__author__ = 'serhii'
import math

class Position():

    x = 0
    y = 0
    z = 0

    rotation = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get_position(self):
        return (self.x, self.y, self.z)


    def set_position(self, x_axe, y_axe, z_axe=0):
        self.x = x_axe
        self.y = y_axe
        self.z = z_axe

        return True

    def planar_distance_to(self, pos_b):
        """
        Measures distance in horisontal plane
        :param pos_b: Possition object to which distance is measured
        :return:
        """
        return math.hypot(self.x - pos_b.x, self.y - pos_b.y)

    def distance_to(self, pos_b):
        return math.hypot(self.planar_distance_to(pos_b), self.z - pos_b.z)


    def clone(self):

        return Position(self.x, self.y, self.z)

    def move(self, d_x, d_y, d_z=0):
        self.x += d_x
        self.y += d_y
        self.z += d_z