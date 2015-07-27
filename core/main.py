import logging

from core.primitives.map import Map
from core.primitives.node import Node
from core.primitives.node_bus import NodeBus
from core.primitives.message import Message



def main():

    bus = NodeBus()

    mapDemo = Map()

    mapDemo.add_node(Node())
    mapDemo.list_nodes()

    for n in mapDemo.get_nodes():
        bus.register(n)

    time = 0
    t_step = 1 # us
    sym_duration = 10

    time_line = range(time, sym_duration, t_step)

    while time_line:
        t = time_line.pop(0)
        #print t
        logging.info('Time step: %d' % t)
        bus.broadcast(Message(Message.TIME, t))


if __name__ == "__main__":

    logging.basicConfig(
        #filename='example.log',
        format='[%(levelname)s] / %(asctime)s / %(message)s',
        level=logging.DEBUG
    )

    main()

