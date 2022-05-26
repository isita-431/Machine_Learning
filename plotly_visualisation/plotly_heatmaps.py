# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


dataset = pd.read_csv('okcupid_dataset.csv')

print(dataset.head())
print(dataset.columns)

cols =['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7',
       'col8']

data = [go.Heatmap(x=dataset['y'],y=dataset['x'],z=dataset[cols], colorscale='viridis', showscale=True)]

pyo.plot(data)