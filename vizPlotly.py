import plotly.graph_objects as go

innerBurnLabel = '100 DeltaV'
outerBurnLabel = '200 DeltaV'

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[50, 50],
    y=[35, 95],
    text=[innerBurnLabel,
          outerBurnLabel],
    mode="text",
    showlegend=False,
    textfont={'size': 8}
))

# Inner Orbit Legend Entry
fig.add_trace(go.Scatter(
    x=[None],
    y=[None],
    mode="markers",
    name="Inner Orbit",
    marker=dict(size=7, color="Blue")
))

# Outer Orbit Legend Entry
fig.add_trace(go.Scatter(
    x=[None],
    y=[None],
    mode="markers",
    name="Outer Orbit",
    marker=dict(size=7, color="Green")
))

# Transfer Orbit Legend Entry
fig.add_trace(go.Scatter(
    x=[None],
    y=[None],
    mode="markers",
    name="Transfer Orbit",
    marker=dict(size=7, color="Red")
))

# Set axes properties
fig.update_xaxes(range=[0, 120], zeroline=False, visible=True)
fig.update_yaxes(range=[0, 120], visible=True)


# Outer Orbit
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=10, y0=10, x1=90, y1=90,
    line_color="Green",
)

# Inner Orbit
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=40, y0=40, x1=60, y1=60,
    line_color="Blue",
)

# Orbital Body
fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="DarkGrey",
    x0=48, y0=48, x1=52, y1=52,
    line_color="DarkGrey",
)

# Transfer orbit 
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=30, y0=40, x1=70, y1=90,
    line_color="Red",
    line_dash="dash"
)


# Set figure size
fig.update_layout(width=800, height=800, showlegend=True)

fig.show()