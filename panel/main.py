__author__ = 'Serhii Kashuba kashubasv@gmail.com'
import json

from flask import Flask
from flask import render_template

from core.demo import demo_map
from core.primitives.node import Node
from core.utils.rf_model import rfModel
from core.utils.nn_path_planner import NNPathPlanner

from core.utils import position
app = Flask(__name__)

def run():
    app.run(debug=True)


@app.route("/")
def map():
    map = demo_map()

    nodes_data = []

    uav = Node("uav", 400, 400, 150)

    f = 868*1000000
    rf = rfModel()

    uav_altitude = 200
    uav_start = position.Position(0, 0, uav_altitude)

    nodes = map.get_nodes()
    to_visit = []
    for node in nodes:
        to_visit.append(node.get_position(True))

    planner = NNPathPlanner()


    uav_path = planner.compute_path(uav_start, to_visit)

    #uav_path = planner.reduce_path(200, 1)

    uav_path = planner.reduce_path(200, 5)

    #uav_path.extend(uav_path_2)


    dynamic_data = []
    # time dynamic data
    for (x, y, z) in [p.get_position() for p in uav_path]:
        nodes_state = []
        uav.set_position(x, y, uav_altitude)

        for node in nodes:
            node_info = dict()
            node_info['id'] = node.get_name()
            node_info['position'] = node.get_position()
            node_info['snr'] =  rf.attenuation(f, uav.distance_to(node), rf.DB)
            nodes_state.append(node_info)

        state = {'position': (x, y, uav_altitude), 'nodes': nodes_state}
        dynamic_data.append(state)

    uav_data = {'id': "uav", 'position': uav.get_position()}
    uavs_data = [uav_data]

    params = {
        "title": "main",
        "nodes": nodes,
        "nodes_data": json.dumps(nodes_data),
        "uavs_data": json.dumps(uavs_data),
        "dynamic_data": json.dumps(dynamic_data),

    }
    return render_template("index.html", **params)


if __name__ == "__main__":
    run()
