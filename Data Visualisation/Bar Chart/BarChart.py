import plotly.graph_objects as go
import numpy as np

np.random.seed(42)

# declaring size of arr
size = 7

x = [f'Product {i}' for i in range(size)]
y = np.random.randint(low=0, high=100, size=size)

# creating the Bar Chart
fig = go.Figure(go.Bar(
    x=x,
    y=y,
    text=y,
    textposition='outside',
    marker_color='indianred',
    hovertemplate="%{x} : %{y} <extra></extra>",
    showlegend=False,
))

# Modifying the tickangle of the xaxis, and adjusting width and height of the image
fig.layout.template = 'plotly_dark'
# Hiding y-axis labels
layout_yaxis_visible = False
layout_yaxis_showticklabels = False
fig.update_layout(
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    xaxis_tickangle=-45,
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
# Removing the background grid and the Y-axis labels
fig.update_yaxes(showgrid=False, showticklabels=False)

fig.show()