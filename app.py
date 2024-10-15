from opensky_api import OpenSkyApi
from flask import Flask, render_template
from scripts.welcome_maps import welcome_map
from scripts.flight_path import flight_path
from scripts.opensky import get_states
from scripts.map_flights import map_flights

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/all_crafts")
def all_crafts():
    map_html = map_flights(get_states(OpenSkyApi()))
    return render_template("index.html", map_html=map_html)


@app.route("/flight_path/<icao24>/<color>")
def craft_details(icao24, color):
    map_html = flight_path(icao24, color)
    return render_template("index.html", map_html=map_html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
