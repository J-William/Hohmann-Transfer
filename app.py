from flask import Flask, request, render_template

from visualization import build_viz

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return '<p>post received</p>'
    
    return render_template('index.html', visualization=build_viz())

