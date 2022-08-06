# import packages
import numpy as np
import plotly.offline as pyo
import  plotly.graph_objs as go
import pandas as pd

np.random.seed(101)

x = np.random.randint(1,51,50)
y = np.random.randint(1,51,50)

data = [go.Scatter(x=x,y=y,mode='markers',
                   marker = dict(size = 12, color = 'rgb(51,205,153)', symbol ='circle', line= {'width':2}))]

layout = go.Layout(title ='scatter plot', xaxis = dict(title= 'x-axis'), yaxis = dict(title = 'y-axis'), hovermode='closest')
fig = go.Figure(layout=layout,data = data)
pyo.plot(fig,filename = 'basic_scatter_plot.html')



