# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

#import data from tips.csv and create histogram plots for the tips and the total bill column.
# start = 0 , stop 20, size  = 2
dataset = pd.read_csv('tips.csv')

# create a traces for the histogram, plot
data =[go.Histogram(x=dataset['total_bill'], xbins=dict(start=0,end=50,size=2))]

# creating a layout
layout= go.Layout(title = 'histogram')
# creating a figure

fig= go.Figure(layout=layout,data=data)


# plotting the data
pyo.plot(fig)