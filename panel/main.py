__author__ = 'Serhii Kashuba kashubasv@gmail.com'
import json

from flask import Flask
from flask import render_template

from core.demo import demo_map
from core.primitives.node import Node
from core.utils.rf_model import rfModel

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
    uav_path = [
        (0, 0),
        (200, 200),
        (400, 400),
        (500, 700),
        (600, 950),
        (700, 1000)
    ]

    nodes = map.get_nodes()
    for node in nodes:
        #(x, y, z) = node.get_position()
        node_info = dict()
        node_info['id'] = node.get_name()
        node_info['position'] = node.get_position()
        node_info['snr'] =  rf.attenuation(f, uav.distance_to(node), rf.DB)

        nodes_data.append(node_info)

    dynamic_data = []
    for (x, y) in uav_path:
        dynamic_data.append({'position': (x,y,uav_altitude)})

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
