# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


#create 5 random points

x=[1, 2, 3, 4,5]
y=[10, 11, 12, 13,14]
# create a trace for the bubble plot , mention size and colour

trace = [go.Scatter(x=x,y=y,mode='markers', marker=dict(color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
                                                   'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
                    opacity=[1, 0.8, 0.6, 0.4],
                    size=[40, 60, 80, 100]))]


# create a layout
layout = go.Layout(title='bubble plot',hovermode = 'closest')

# create a figure
fig = go.Figure(data=trace, layout=layout)

# plot the bubble plot
pyo.plot(fig, 'bubble_chart.html')