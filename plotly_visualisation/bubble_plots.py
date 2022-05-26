# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

dataset = pd.read_csv('gapminderDataFiveYear.csv')

dataset = dataset[dataset['year']==2007]

print(dataset.head())

trace = [go.Scatter(x=dataset['gdpPercap'], y= dataset['lifeExp'], mode='markers',text=dataset['country'], marker = dict(color = dataset['lifeExp'],
                    size = dataset['pop']/5000000 , sizemin =4, colorscale= 'viridis',showscale = True))]

layout = go.Layout(title='bubble plot', xaxis= {'title':'gdpPercap'}, yaxis = dict(title = 'life expectancy'))


fig = go.Figure(layout=layout,data = trace)

pyo.plot(fig, filename='bubble_plot.html')