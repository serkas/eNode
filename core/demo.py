__author__ = 'Serhii Kashuba kashubasv@gmail.com'
import random

from primitives.map import Map
from primitives.node import Node

def demo_map():
    mapDemo = Map()

    nodes = {
        1: (12, 45, 0),
        2: (23, 21, 0),
        3: (45, 87, 0),
    }

    nodes = generate_nodes_data(50, 2000, 2000)

    for nid in nodes:
        position =  nodes[nid]
        mapDemo.add_node(Node(nid, *position))


    #print mapDemo
    return mapDemo


def generate_nodes_data(number, x_max, y_max):
    nodes = dict()
    for node_id in xrange(number):
        nodes[node_id] = (random.randint(0, x_max), random.randint(0, y_max), 0)
    return nodes