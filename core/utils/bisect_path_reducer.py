__author__ = 'Serhii Kashuba kashubasv@gmail.com'

import math

from core.utils.position import Position
from core.utils.path_reducer import PathReducer

import core.utils.geometry as geometry

class BisectPathReducer(PathReducer):

    def move_in_range(self, a, b, c, r):
        min_d = a.planar_distance_to(b)
        #print  min_d

        max_d = a.planar_distance_to(c) + c.planar_distance_to(b)
        #print max_d
        best_position = c


        a_direction = c.azimuth(a)
        b_direction = c.azimuth(b)

        if b_direction < a_direction:
            b_direction, a_direction = a_direction, b_direction

        optimal_line_direction = 1.0 *(a_direction + b_direction) / 2

        candidates = []

        d_x = r * math.sin(optimal_line_direction)
        d_y = -r * math.cos(optimal_line_direction)

        #print optimal_line_direction * 180/ math.pi
        #print d_x, d_y

        d = c.clone().move(d_x, d_y)
        e = c.clone().move(-d_x, -d_y)

        candidates.append(d)
        candidates.append(e)

        # point on AB
        intersection = geometry.line_intersection(a, b, c, d)
        #print intersection
        if intersection:
            p = Position(*intersection)
            if c.planar_distance_to(p) < r:
                candidates.append(p)

        for candidate in candidates:
            dist = a.planar_distance_to(candidate) + candidate.planar_distance_to(b)
            #print dist, candidate.get_position()

            if dist < max_d:
                max_d = dist
                best_position = candidate

        #print a.get_position(), b.get_position(), c.get_position(), d.get_position()


        #print c.azimuth(b)
        #print optimal_line_direction, c.get_position()
        #print '='*20
        return best_position



if __name__ == "__main__":

    a = Position(0,0)
    b = Position(200, 0)

    c = Position(150, 150)

    red = BisectPathReducer()

    red.move_in_range(a, b, c, 50)