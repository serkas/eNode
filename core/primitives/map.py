__author__ = 'serhii'

from core.primitives.primitive import Primitive

class Map(Primitive):

    nodes = []
    node_names = set()


    def __init__(self):
        pass

    def add_node(self, new_node):
        name = new_node.get_name()

        if(name in self.node_names):
            return False
        else:
            self.nodes.append(new_node)
            self.node_names.add(name)
            return True

    def get_nodes(self):
        return self.nodes

    def list_nodes(self):
        self.log("List of nodes on map:")

        for i, node in enumerate(self.nodes):
            self.log( "%d. %s" % (i, node.get_name()))


    def get_nodes_count(self):
        return len(self.nodes)