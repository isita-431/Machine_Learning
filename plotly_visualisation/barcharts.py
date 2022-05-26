
# importing packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

dataset = pd.read_csv('tips.csv')
print(dataset.head())

trace0 = go.Bar(x=dataset['sex'], y=dataset['tip'])
trace1 = go.Bar(x=dataset['sex'], y=dataset['total_bill'])
data = [trace0,trace1]

layout = go.Layout(title='tips data', barmode='stack')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig,filename='barchart.html')