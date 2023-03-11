import base64
from io import BytesIO
from matplotlib.patches import Circle, Ellipse
from matplotlib.figure import Figure

FIGURE_CENTER = (50, 50)
FIGSIZE = (10, 10)
FIG_SCALE = {'xMin': 0, 'xMax': 100, 'yMin': 0, 'yMax': 100}


def burn_annotation(initial, target, delta):
    return "Initial Velocity: {}\nTarget Velocity: {}\nDeltaV: {}".format(initial, target, delta)

def build_viz(maneuver=None):  
    fig = Figure(figsize=FIGSIZE)
    ax = fig.subplots()
    ax.set_xlim(FIG_SCALE['xMin'], FIG_SCALE['xMax'])
    ax.set_ylim(FIG_SCALE['yMin'], FIG_SCALE['yMax'])

    low_radius = 10
    high_radius = 40

    orbitalBodyArtist = Circle(
        FIGURE_CENTER,
        5,
        fill = True
    )

    lowerOrbitArtist = Circle( 
        FIGURE_CENTER,
        low_radius,
        fill = False 
    )

    higherOrbitArtist = Circle(
        FIGURE_CENTER,
        high_radius,
        fill = False
    )

    # if maneuver:
    a = (low_radius + high_radius) / 2
    b = abs(low_radius - high_radius) / 2
    
    transferOrbitArtist = Ellipse(
        (50, 65),
        2 * a,
        2 * b,
        90,
        linestyle='dotted',
        edgecolor='r',
        fill=False
    )
    ax.add_artist(transferOrbitArtist)
    
    ax.annotate(burn_annotation(50, 100, 50), xy=(50, 40), xytext=(40, 20), arrowprops=dict(arrowstyle="->",facecolor='blue'))
    ax.annotate(burn_annotation(50, 100, 50), xy=(50, 90), xytext=(15, 90), arrowprops=dict(arrowstyle="->",facecolor='blue'))

    
    ax.add_artist(orbitalBodyArtist)
    ax.add_artist(lowerOrbitArtist)
    ax.add_artist(higherOrbitArtist)
    
    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"