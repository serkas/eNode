__author__ = 'Serhii Kashuba kashubasv@gmail.com'


import unittest

from primitives.map import *
from primitives.node import *


class NodeTest(unittest.TestCase):
    def setUp(self):
        print "Creating a new Node..."
        self.node = Node()

    def tearDown(self):
        pass

    def test_node_position(self):
        self.node.set_position(12, 15, -2)

        self.assertEquals(self.node.get_position(), (12, 15, -2))


    def test_nodes_distance(self):
        node2 = Node()
        node2.set_position(3, 4, 0)

        self.assertEquals(self.node.distance_to(node2), 5)

if __name__ == "__main__":
    unittest.main()
