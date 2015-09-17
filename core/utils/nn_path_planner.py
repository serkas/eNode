__author__ = 'Serhii Kashuba kashubasv@gmail.com'

import math
from path_planner import PathPlanner

from core.utils.position import Position

class NNPathPlanner(PathPlanner):
    """
    Nearest neighbor path planner
    Simple and coarse heuristic solution for Travelling Salesmen Problem
    """

    def compute_distances(self, start):
        # init matrix
        n = len(self.nodes)
        for x in xrange(n):
            self.distances.append([0 for x in xrange(n)])
            self.start_distances.append(0)

        # all pairs of nodes
        for i in xrange(n):
            for j in xrange(i+1, n):
                node_a = self.nodes[i]
                dist = node_a.planar_distance_to(self.nodes[j])
                self.distances[i][j] = dist
                self.distances[j][i] = dist

        # distances from start point
        for i in xrange(n):
            node_a = self.nodes[i]
            dist = node_a.planar_distance_to(start)
            self.start_distances[i] = dist

    def get_closest(self, distances, exclude=set()):
        candidate = -1
        curr_distance = float('inf')

        # print exclude
        for i, distance in enumerate(distances):

            if i not in exclude and distance < curr_distance:
                candidate = i
                curr_distance = distance

        return candidate

    def compute_path(self, start, to_visit):
        
        self.enumerate_nodes(to_visit)

        self.compute_distances(start)

        visited = set()

        self.path.append(start)

        # first
        self.position = self.get_closest(self.start_distances)

        visited.add(self.position)
        self.path.append(self.nodes[self.position])

        # rest of nodes
        while len(visited) < len(self.nodes):
            from_current = self.distances[self.position]

            self.position = self.get_closest(from_current, visited)
            visited.add(self.position)
            self.path.append(self.nodes[self.position])

        return self.path

