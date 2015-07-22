__author__ = 'Serhii Kashuba kashubasv@gmail.com'

import unittest

from core.primitives.map import *
from core.primitives.node import *

class MapTest(unittest.TestCase):
    def setUp(self):
        print "Creating a new Map..."
        self.map = Map()

    def tearDown(self):
        pass

    def test_add_node(self):
        node = Node()
        self.map.add_node(node)
        self.assertEquals(self.map.get_nodes_count(), 1)



if __name__ == "__main__":
    unittest.main()
