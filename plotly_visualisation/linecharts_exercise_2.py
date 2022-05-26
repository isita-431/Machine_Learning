import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

data = pd.read_csv('2016-weather-data-seattle.csv')
x = data['Date']

cols = ['Max_TemperatureC','Mean_TemperatureC','Min_TemperatureC']
print(data.head())

l=[]
# using for loop
for i in cols:
    trace = go.Scatter(x=x, y= data[i], mode='lines',name =i)
    l.append(trace)
layout = go.Layout(title= 'weather_seattle', xaxis = dict(title='Date'), yaxis= dict(title= 'Temperature'))
fig = go.Figure(data=l,layout=layout)
pyo.plot(fig,filename='one.html')

# using list comprehension
data = [go.Scatter(x=x,y=data[name], mode = 'lines',name= name) for name in cols]
pyo.plot(data,filename='two.html')