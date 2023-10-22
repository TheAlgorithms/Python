import plotly.graph_objects as go
import numpy as np

# X , Y , Z cordinates
x_cord = np.arange(0, 50, 2)
y_cord = np.arange(0, 50, 2)
z_function = np.sin((x_cord + y_cord)/2)

fig = go.Figure(data=go.Contour(x=x_cord,
                                y=y_cord,
                                z=z_function,
                                colorscale='darkmint',
                                contours=dict(
                                    showlabels=False,  # show labels on contours
                                    labelfont=dict(  # label font properties
                                        size=12,
                                        color='white',
                                    )
                                ),
                                colorbar=dict(
                                    thickness=25,
                                    thicknessmode='pixels',
                                    len=1.0,
                                    lenmode='fraction',
                                    outlinewidth=0,
                                    title='Title',
                                    titleside='right',
                                    titlefont=dict(
                                        size=14,
                                        family='Arial, sans-serif')

                                ),

                                )
                )

fig.update_layout(
    title='Contour Plot',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title',
    autosize=False,
    width=900,
    height=600,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)

fig.layout.template = 'plotly_dark'
fig.show()
