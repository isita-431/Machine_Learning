# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff


#create your own data
x = ['teamA','teamB','teamC']
y = ['MON',"TUE", "WED","THUR","FRI","SAT","SUN"]
z = [[10,2,20],[20,15,9],[8,6,10],[19,30,20],[12,10,20],[12,18,10],[19,19,11]]

# create a trace for the heatmap

data = [go.Heatmap(x=x,y=y, z=z,
                   colorscale='viridis',
                   showscale=True)]


# create a layout
layout = go.Layout(title='% of work done')

# create a figure
fig = go.Figure(data=data,layout=layout)

# plot the heatmap
pyo.plot(fig)
