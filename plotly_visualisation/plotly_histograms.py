# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


# importing data
dataset = pd.read_csv('2016-weather-data-seattle.csv')

print(dataset.head())

# creating histogram trace
data = [go.Histogram(x=dataset['Max_TemperatureC'],xbins=dict(start=0,end=40,size=2))]

# creating a layout
layout= go.Layout(title='histogram')

# creating a figure
fig = go.Figure(layout=layout,data=data)

# plotting the data
pyo.plot(fig)