import plotly.graph_objects as go
import numpy as np

np.random.seed(1)

# declaring size of arr
size = 10
size_arr = np.random.randint(low=50, high=600, size=size)

x = np.random.randint(low=0, high=30, size=size)
y = np.random.randint(low=0, high=20, size=size)

fig = go.Figure(
    data=[
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=dict(
                size=size_arr,
                sizemode="area",
                sizeref=2.0 * max(size_arr) / (40.0**2),
                sizemin=4,
            ),
            hovertemplate=" x : %{x} <br> y : %{y} <br>",
        )
    ]
)

# Adjusting width and height of the image
fig.layout.template = "plotly_dark"
fig.update_layout(
    title="Bubble Chart",
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
)


fig.show()
