# import packages
import numpy as np
import plotly.offline as pyo
import  plotly.graph_objs as go
import pandas as pd

x = np.linspace(0,50,100)
y = np.random.rand(50)

trace0 = go.Scatter(x=x,y=y+5,mode ='markers', name = 'scatterplot')
trace1 = go.Scatter(x=x,y=y,mode ='lines', name = 'lineplot')
trace2 = go.Scatter(x=x,y=y-3,mode ='lines+scatter', name = 'lineplot')

data = [trace0,trace1]

layout = go.Layout(title = 'line charts',xaxis = dict(title= 'x-axis'), yaxis = dict(title = 'y-axis'))

fig = go.Figure(data = data ,layout=layout)

pyo.plot(fig, filename='line.html')
