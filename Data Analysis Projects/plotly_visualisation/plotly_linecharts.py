import numpy as np
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

dataset = pd.read_csv('timeseries.csv')
x = dataset['Date']

cols =['A','B','C','D','E','F','G']


data =[go.Scatter(x=x,y=dataset[name],mode='lines',name=name) for name in cols]

pyo.plot(data,filename='line_chart.html')
