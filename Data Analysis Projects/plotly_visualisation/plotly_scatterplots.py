# import the packages
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

dataset = pd.read_csv('headbrain1.csv')


x = dataset['Head Size(cm^3)']
y= dataset['Brain Weight(grams)']


data = [go.Scatter(x=x,y=y, mode = 'markers',marker = dict(size=12, color ='green', symbol ='circle', line={'width':2}))]

layout = go.Layout(title='scatter plot', xaxis={'title':'head size '}, yaxis= dict(title='brain weight'), hovermode='closest')

fig = go.Figure(layout=layout,data=data)

pyo.plot(fig,filename='scatter_plot.html')