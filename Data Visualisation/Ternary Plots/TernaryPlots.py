import plotly.express as px
import plotly.graph_objects as go

df = px.data.election()

fig = go.Figure(go.Scatterternary({
    'mode': 'markers',
    'a': df['Joly'],
    'b': df['Coderre'],
    'c': df['Bergeron'],
    'marker': {
        'color': 'green',
        'size': 14,
    },

}))
fig.update_layout({
    'title': 'Ternary Scatter Plot',
    'ternary':
        {
            'sum': 1,
            'aaxis': {'title': 'Joly', 'min': 0.01, 'linewidth': 2, 'ticks': 'outside'},
            'baxis': {'title': 'Coderre', 'min': 0.01, 'linewidth': 2, 'ticks': 'outside'},
            'caxis': {'title': 'Bergeron', 'min': 0.01, 'linewidth': 2, 'ticks': 'outside'}
        },
    'showlegend': False
})

fig.layout.template = 'plotly_dark'
fig.show()
