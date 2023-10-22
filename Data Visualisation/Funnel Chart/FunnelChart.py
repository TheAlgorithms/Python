from plotly import graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Funnel(
        name="India",
        y=["McDonalds", "Dominoz", "PizzaHut", "Subway", "MadOverDonuts", "Keventers"],
        x=[150, 140, 40, 50, 40, 20],
        textposition="inside",
        textinfo="value+percent initial",
    )
)

fig.add_trace(
    go.Funnel(
        name="Bangladesh",
        orientation="h",
        y=["McDonalds", "Dominoz", "PizzaHut", "Subway"],
        x=[50, 60, 40, 30],
        textposition="inside",
        textinfo="value+percent previous",
    )
)

fig.add_trace(
    go.Funnel(
        name="SriLanka",
        orientation="h",
        y=["McDonalds", "Dominoz", "PizzaHut", "Subway", "MadOverDonuts"],
        x=[90, 70, 50, 30, 10],
        textposition="outside",
        textinfo="value+percent total",
    )
)

fig.update_layout(
    title="Funnel Chart for Food Sales in Asian Countries", showlegend=True
)
fig.layout.template = "plotly_dark"
fig.show()
