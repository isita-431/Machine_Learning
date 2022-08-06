# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go


#import data from tips.csv and create bar plots for the tips and the total bill column.

dataset = pd.read_csv('tips.csv')

# create a traces for the box plot
data = [go.Box(y=dataset['total_bill'],boxpoints='all',jitter=1, pointpos=0, name = 'total_bill'),
        go.Box(y=dataset['tip'],boxpoints='all',jitter=1, pointpos=0 , name='tips')]


# create a layout
layout = go.Layout(title='box plot')

# create a figure
fig = go.Figure(data=data,layout=layout)

# plot the bar plot
pyo.plot(fig, filename='plotly_box_plot_exercise.html')
