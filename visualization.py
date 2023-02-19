import base64
from io import BytesIO
from matplotlib.patches import Circle
from matplotlib.figure import Figure

def build_viz():
    FIGURE_CENTER = (50, 50)
    
    fig = Figure(figsize=(10, 10))
    ax = fig.subplots()

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
 
    ax.add_artist(orbitalBodyArtist)
    ax.add_artist(initialOrbitArtist)
    ax.add_artist(targetOrbitArtist)

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    buf = BytesIO()
    fig.savefig(buf, format="png")

    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"