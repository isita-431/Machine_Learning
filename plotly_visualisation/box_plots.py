# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# randomly creating data
team_A= np.random.randint(1,100,30)
team_B = np.random.randint(1,100,30)

# box plots
trace0 = go.Box(y=team_A,boxpoints='all',jitter=0.5, pointpos=0)
trace1 = go.Box(y=team_B,boxpoints='all',jitter=1,pointpos=0)
data = [trace0,trace1]

layout = go.Layout(title='box plot')

fig= go.Figure(data=data,layout=layout)

pyo.plot(fig)


