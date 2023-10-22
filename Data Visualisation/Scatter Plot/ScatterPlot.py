import plotly.express as px
import numpy as np

np.random.seed(42)

# declaring size of arr
size = 100

x = np.random.randint(low=0, high=100, size=size)
y = np.random.randint(low=0, high=100, size=size)

fig = px.scatter(x=x, y=y)

# Adjusting width and height of the image
fig.layout.template = "plotly_dark"
fig.update_layout(
    title="Scatter Plot",
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
)
fig.show()
