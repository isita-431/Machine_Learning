# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

#import data from tips.csv and create distplots for the tips and the total bill column.
dataset = pd.read_csv('tips.csv')


# create a traces for the distplot
hist_data = [dataset['total_bill'], dataset['tip']]
group_labels = ['total_bill','tips']

# create a figure
fig = ff.create_distplot(hist_data = hist_data ,group_labels=group_labels, bin_size=[1,2])


# plot the histogram plot
pyo.plot(fig)
