__author__ = 'Serhii Kashuba kashubasv@gmail.com'

from flask import Flask
from flask import render_template

from core.demo import demo_map


app = Flask(__name__)

def run():
    app.run(debug=True)


@app.route("/")
def map():
    map = demo_map()

    plot_data = []

    nodes = map.get_nodes()
    for node in nodes:
        (x, y, z) = node.get_position()
        plot_data.append([x, y, 0.5])

    params = {"title": "main", "nodes": nodes, "plot_data": plot_data}
    return render_template("index.html", **params)


if __name__ == "__main__":
    run()
