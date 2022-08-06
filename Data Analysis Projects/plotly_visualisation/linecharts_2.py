# linecharts part 2
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

data = pd.read_csv('timeseries.csv')
x = data['Date']

cols = ['A','B','C','D','E','F','G']
print(data.head())

data = [go.Scatter(x=x,y=data[name],mode = 'lines',name=name ) for name in cols ]
pyo.plot(data)