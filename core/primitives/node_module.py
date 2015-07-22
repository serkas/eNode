__author__ = 'serhii'

from core.primitives.primitive import Primitive


class NodeModule(Primitive):

    core = None

    def set_core(self, core_node):
        self.core = core_node
