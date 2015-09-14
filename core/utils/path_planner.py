__author__ = 'Serhii Kashuba kashubasv@gmail.com'


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

        move_limit = 1

        for index, p in enumerate(self.path):
            if index == 0 or index == len(self.path) - 1 or move_limit <= 0:
                # don't touch first and last yet
                self.reduced_path.append(p.clone())

            else:
                prev = self.path[index-1]
                next = self.path[index+1]

                move_limit -= 1

        return self.reduced_path
