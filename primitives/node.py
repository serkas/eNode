__author__ = 'serhii'

from primitives.primitive import *
from primitives.position import *
from primitives.rf_module import *

class Node(Primitive):
    p_type = "node"
    name = "default"
    id = 0

    position = None
    rf = None

    def __init__(self):

        self.apply_config(self.get_config(self.p_type, self.name))

        self.rf = RfModule()
        self.rf.set_core(self)

        if "rf" in self.config:
            self.rf.apply_config(self.config["rf"])



        self.position = Position()


    def get_name(self):
        return "%s_%d" % (self.name, self.id)


    def get_position(self):
        return self.position.get_position()