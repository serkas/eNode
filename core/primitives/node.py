__author__ = 'serhii'

from core.primitives.primitive import Primitive
from core.primitives.rf_module import RfModule
from core.utils.position import Position
from core.primitives.message import Message

class Node(Primitive):

    p_type = "node"
    name = "default"
    id = 0

    position = None
    rf = None

    def __init__(self, id=0, x=0, y=0, z=0):
        """
        Node constructor
        :param id: unique node identifier
        :param x: position x (meters)
        :param y: position y (meters)
        :param z: altitude (meters)
        :return:
        """
        self.apply_config(self.get_config(self.p_type, self.name))
        self.id = id
        self.rf = RfModule()
        self.rf.set_core(self)

        if "rf" in self.config:
            self.rf.apply_config(self.config["rf"])

        self.position = Position()

        self.set_position(x, y, z)


    def get_name(self):
        return "%s_%d" % (self.name, self.id)

    def set_position(self, x, y, z=0):
        self.position.set_position(x, y, z)

    def get_position(self, return_obj=False):
        if return_obj:
            return self.position
        return self.position.get_position()

    def distance_to(self, node_b):
        return self.position.distance_to(node_b.position)

    def accept(self, message):
        if message.type_of(Message.TIME):
            self.log("get time")