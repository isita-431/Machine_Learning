# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# import the csv file
# csv file to be imported is 2018WinterOlympics.csbv
data= pd.read_csv('2018WinterOlympics.csv')
cols =['NOC','Gold','Silver','Bronze','Total']
print(data.head())
# create a stacked bar chart and a nested bar chart
data = [go.Bar(x=data['NOC'], y=data[name], name =name) for name in cols]


# create a layout
layout = go.Layout(title='Bar plot',barmode='stack')

# plot the bar plot
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig,filename='bar_chart_sol.html')