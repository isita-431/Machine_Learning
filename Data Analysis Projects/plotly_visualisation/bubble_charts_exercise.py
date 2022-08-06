# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


#create 5 random points
x =[1,2,3,4,5]
y = [10,11,12,13,14]

# create a trace for the bubble plot , mention size and colour
trace = [go.Scatter(x=x,y=y, mode='markers',
                    marker = dict(color =['red','green','purple','blue','orange'], opacity=[1,0.8,0.6,0.4],
                    size =[40,60,80,100,120]))]


# create a layout
layout = go.Layout(title ='bubble plot exercise', hovermode='closest')

# create a figure
fig = go.Figure(data=trace,layout=layout)

# plot the bubble chart
pyo.plot(fig, filename='bubble_chart_exercise.html')


