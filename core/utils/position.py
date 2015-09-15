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

    def get(self, coord):

        assert coord in ['x', 'y', 'z'], "Try to get undefined coordinate"

        if coord == "x":
            return self.x
        elif coord == "y":
            return self.y
        elif coord == "z":
            return self.z
        return None

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

        return self


    def azimuth(self, b, deg=False):
        distance = self.planar_distance_to(b)


        if distance <= 0:
            raise Exception('Zero distance in azimuth computation')

        d_x = b.x - self.x
        d_y = b.y - self.y

        rad = abs(math.asin(d_x/distance))

        adapted = 0
        if d_x < 0:
            if d_y < 0:
                adapted = 2*math.pi - rad
            else:
                adapted = math.pi + rad

        else:
            if d_y > 0:
                adapted = math.pi - rad
            else:
                adapted = rad

        #print rad
        if deg:
            return adapted * 180 / math.pi

        return adapted






if __name__ == "__main__":
    eps = 2
    a = Position(0, 0)
    b = Position(0, 40)

    test = [
        (0, -10, 0),
        (10, -100, 6),
        (0, 40, 180),
        (20, 20, 135),

    ]
    for (x,y, estimate) in test:
        #print a.azimuth(Position(x, y))
        assert abs(a.azimuth(Position(x, y)) - estimate) < eps
