__author__ = 'serhii'

from core.primitives.primitive import Primitive
from core.primitives.node_module import *


class EnergyModule(NodeModule):

    p_type = "energy"
    name = "default"

    def __init__(self):
        self.apply_config()


    def get_capacity(self):
        return 1



