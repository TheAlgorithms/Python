import plotly.graph_objects as go
import numpy as np


def create_line_chart(x_data, y_data):
    fig = go.Figure(data=go.Scatter(x=x_data, y=y_data))

    # Modifying the tickangle of the xaxis, and adjusting width and height of the image
    fig.layout.template = 'plotly_dark'
    fig.update_layout(
        title='Line Chart',
        xaxis_title='X Axis Title',
        yaxis_title='Y Axis Title',
        xaxis_tickangle=-45,
        autosize=False,
        width=600,
        height=600,
        margin=dict(l=50, r=50, b=100, t=100, pad=4)
    )
    fig.show()


if __name__ == "__main__":
    np.random.seed(42)

    # Generating sample data
    x_data = np.arange(10)
    y_data = x_data ** 2

    try:
        create_line_chart(x_data, y_data)
    except Exception as e:
        print("An error occurred:", str(e))
