__author__ = 'Serhii Kashuba kashubasv@gmail.com'

import math

from core.utils import position

class PathPlanner:

    nodes = dict()
    distances = []
    start_distances = []
    path = []
    position = -1
    reduced_path = []

    def __init__(self):
        self.nodes = dict()
        self.distances = []
        self.start_distances = []
        self.path = []
        self.position = -1

    def enumerate_nodes(self, to_visit):
        for i, node in enumerate(to_visit):
            self.nodes[i] = node


    def compute_path(self, start, to_visit):
        return [start, (200, 200)]


    def reduce_path(self, radio_distance):

        move_limit = 10000

        for index, p in enumerate(self.path):
            if index == 0 or index == len(self.path) - 1 or move_limit <= 0:
                # don't touch first and last yet
                self.reduced_path.append(p.clone())

            else:
                prev = self.path[index-1]
                next = self.path[index+1]

                new = self.move_in_range(prev, next, p, 200)
                self.reduced_path.append(new)

                move_limit -= 1

        return self.reduced_path


    def move_in_range(self, a, b, c, r):
        min_d = a.planar_distance_to(b)
        #print  min_d

        max_d = a.planar_distance_to(c) + c.planar_distance_to(b)
        #print max_d

        angles = range(0, 360)

        best_position = c

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


