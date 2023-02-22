import base64
from io import BytesIO
from matplotlib.patches import Circle
from matplotlib.figure import Figure

FIGURE_CENTER = (50, 50)
FIGSIZE = (10, 10)
FIG_SCALE = {'xMin': 0, 'xMax': 100, 'yMin': 0, 'yMax': 100}


def build_viz():  
    fig = Figure(figsize=FIGSIZE)
    ax = fig.subplots()
    ax.set_xlim(FIG_SCALE['xMin'], FIG_SCALE['xMax'])
    ax.set_ylim(FIG_SCALE['yMin'], FIG_SCALE['yMax'])

    orbitalBodyArtist = Circle(
        FIGURE_CENTER,
        5,
        fill = True
    )

    initialOrbitArtist = Circle( 
        FIGURE_CENTER,
        7.5,
        fill = False 
    )

    targetOrbitArtist = Circle(
        FIGURE_CENTER,
        50,
        fill = False
    )

    transferOrbitArtist = None
    
    ax.add_artist(orbitalBodyArtist)
    ax.add_artist(initialOrbitArtist)
    ax.add_artist(targetOrbitArtist)
    
    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"