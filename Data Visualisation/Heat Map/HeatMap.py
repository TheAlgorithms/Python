import plotly.express as px
import numpy as np

np.random.seed(42)

# declaring the size of an array
rows = 5
columns = 3

data = np.random.randint(low=0, high=50, size=(columns, rows))

fig = px.imshow(
    data,
    labels=dict(x="X Axis Title", y="Y Axis Title", color="Productivity"),
    x=[f"Product {i}" for i in range(rows)],
    y=[f"Type {i}" for i in range(columns)],
)

# Modifying the tickangle of the xaxis, and adjusting width and height of the image
fig.layout.template = "plotly_dark"
fig.update_xaxes(side="top")
fig.update_layout(
    title="Heat Map ",
    xaxis_tickangle=-45,
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4),
)
fig.show()
