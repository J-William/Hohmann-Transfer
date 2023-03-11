from flask import Flask, request, render_template
from HohmannCalculator import HohmannCalculator as HCal
from visualization import build_viz

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        h = HCal(orbital_body_mass=float(request.form["orbital-body-mass"]))

        maneuver = {
            "initial_radius": float(request.form["initial-orbit"]),
            "target_radius": float(request.form["target-orbit"]),
        }

        maneuver.update(
            h.calculate(maneuver["initial_radius"], maneuver["target_radius"])
        )

        return render_template(
            "index.html", visualization=build_viz(maneuver), maneuver=maneuver
        )

    return render_template("index.html", visualization=build_viz())
