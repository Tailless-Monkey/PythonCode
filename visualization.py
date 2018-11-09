#!/usr/bin/env python
# coding=utf-8
import plotly.plotly as py
from plotly.graph_objs import *

tracel = Scatter(
    x=df['LifeExpectancy'],
    y=df['GNP'],
    text=country_names,
    mode='markers'
)

layout = Layout(
    xaxis=XAxis( title='Life Expectancy'),
    yaxis=YAxis( type='log', title='GNP' )
)

data = Data([trace1])
fig = Figure(data=data, layout=layout)
py.iplot(fig, filename='world GNP vs life expectancy')
