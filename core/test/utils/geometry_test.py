__author__ = 'Serhii Kashuba kashubasv@gmail.com'


import unittest

from core.utils.geometry import *
from core.utils.position import *


class GeometryTest(unittest.TestCase):
    def setUp(self):
        print "Creating a new Nodes ... "
        self.a = Position(0, 0)
        self.b = Position(2, 2)

        self.c = Position(2, 0)
        self.d = Position(1, 1)

    def tearDown(self):
        pass

    def test_intersection(self):

        self.assertEquals(line_intersection(self.a,
                                            self.b,
                                            self.c,
                                            self.d), (1, 1))


        self.assertEquals(line_intersection(Position(5, 0),
                                            Position(5, 12),
                                            Position(0, 2),
                                            Position(1, 4)), (5, 12))

    def test_no_intersection(self):
        self.assertEquals(line_intersection(Position(5, 0),
                                            Position(5, 12),
                                            Position(4, 2),
                                            Position(4, 4)), False)


if __name__ == "__main__":
    unittest.main()
