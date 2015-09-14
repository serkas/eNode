__author__ = 'Serhii Kashuba kashubasv@gmail.com'

import math

from core.utils import position
class PathReducer:

    def move_in_range(self, a, b, c, r):
        min_d = a.planar_distance_to(b)
        max_d = a.planar_distance_to(c) + c.planar_distance_to(b)

        best_position = c

        angles = range(0, 360)
        for angle in angles:
            rad = 1.0 * angle/180 * math.pi
            d_x = math.sin(rad) * r
            d_y = math.cos(rad) * r

            candidate = c.clone()

            candidate.move(d_x, d_y)
            dist = a.planar_distance_to(candidate) + candidate.planar_distance_to(b)
            #print dist, candidate.get_position()

            if dist < max_d:
                max_d = dist
                best_position = candidate


        return best_position


    def test_g(self):
        a = position.Position(0, 0)
        b = position.Position(100, 100)

        c = position.Position(200, 100)

        r = 50

        best_position = self.move_in_range(a, b, c, r)

        print max_d, best_position.get_position()