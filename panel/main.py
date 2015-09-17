__author__ = 'Serhii Kashuba kashubasv@gmail.com'
import json

from flask import Flask
from flask import render_template

from core.demo import demo_map, generate_nodes_data
from core.primitives.node import Node
from core.utils.position import Position
from core.utils.rf_model import rfModel
from core.utils.nn_path_planner import NNPathPlanner

from core.utils import position
app = Flask(__name__)

def run():
    app.run(debug=True)

R = 50

@app.route("/")
def map():
    map = demo_map()

    nodes_data = []
    report = []

    traces = []

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
    report.append({'label': "Nodes path", 'value': planner.path_length(uav_path)})
    traces.append(uav_path)

    uav_path = planner.reduce_path(R, 5)
    report.append({'label': "Reduced path", 'value': planner.path_length(uav_path)})
    #uav_path.extend(uav_path_2)
    traces.append(uav_path)

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

    serial_traces = []
    for path in traces:
        serial_traces.append([p.get_position() for p in path])

    params = {
        "title": "main",
        "nodes": nodes,
        "report": report,
        "nodes_data": json.dumps(nodes_data),
        "uavs_data": json.dumps(uavs_data),
        "dynamic_data": json.dumps(dynamic_data),
        "traces": json.dumps(serial_traces),

    }
    return render_template("index.html", **params)


@app.route("/path")
def path():

    report = []

    traces = []

    uav_altitude = 200
    uav_start = position.Position(0, 0, uav_altitude)

    init_paths = []
    opt_paths = []

    repeats = 1000
    report.append({'label': "Repeats", 'value': repeats})
    for i in range(repeats):
        nodes = generate_nodes_data(10, 2000, 2000)
        to_visit = []
        for node_id in nodes:
            to_visit.append(Position(*nodes[node_id]))

        planner = NNPathPlanner()

        uav_path = planner.compute_path(uav_start, to_visit)
        init_paths.append(planner.path_length(uav_path))

        uav_path_opt = planner.reduce_path(R, 5)
        opt_paths.append(planner.path_length(uav_path_opt))

    avg_init = sum(init_paths)/len(init_paths)
    avg_opt = sum(opt_paths)/len(opt_paths)
    reduction = (avg_init - avg_opt) / avg_init

    report.append({'label': "Init", 'value': avg_init})
    report.append({'label': "Reduced", 'value': avg_opt})

    report.append({'label': "Reduction", 'value': reduction})

    params = {
        "title": "main",
        "nodes": nodes,
        "report": report,
    }
    return render_template("path.html", **params)

if __name__ == "__main__":
    run()
