import plotly.express as px
import numpy as np

np.random.seed(0)

# declaring size of arr
size = 50

data = np.random.randint(low=0, high=150, size=size)
# create the bins
fig = px.histogram(x=data, labels={'x': 'data', 'y': 'count'})

fig.layout.template = 'plotly_dark'
fig.update_layout(
    title='Histogram',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()
