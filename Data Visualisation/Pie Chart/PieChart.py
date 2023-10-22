import plotly.graph_objects as go
import numpy as np

np.random.seed(42)

# declaring size of arr
size = 7

x = [f'Product {i}' for i in range(size)]
y = np.random.randint(low=0, high=100, size=size)

# creating a Pie Chart
fig = go.Figure(data=[go.Pie(labels=x, values=y)])

# Adjusting width and height of the image
fig.layout.template = 'plotly_dark'
# To display labels with the percentage
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    title='Pie Chart',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    autosize=False,
    width=600,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()
