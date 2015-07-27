__author__ = 'Serhii Kashuba kashubasv@gmail.com'

from primitives.map import Map
from primitives.node import Node

def demo_map():
    mapDemo = Map()

    mapDemo.add_node(Node(1))

    node2 = Node(2)
    node2.set_position(12, 18, 0)

    mapDemo.add_node(node2)

    #print mapDemo
    return mapDemo

