# import packages
import numpy as np
import plotly.offline as pyo
import  plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('headbrain1.csv')
x = df['Head Size(cm^3)']
y = df['Brain Weight(grams)']
data2 = [go.Scatter(x=x,y=y,mode='markers',
                    marker = dict(size = 12, color = 'rgb(51,205,153)', symbol ='circle', line= {'width':2}))]

layout2 = go.Layout(title ='scatter plot', xaxis = dict(title= 'x-axis'), yaxis = dict(title = 'y-axis'), hovermode='closest')
fig2 = go.Figure(layout=layout2,data = data2)
pyo.plot(fig2,filename = 'basic_scatter_plot.html')
