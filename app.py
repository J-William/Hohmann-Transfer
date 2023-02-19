from flask import Flask

from visualization import build_transfer_viz

app = Flask(__name__)




@app.route("/")
def test():
    return build_transfer_viz()