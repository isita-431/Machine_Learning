# import the packages
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.figure_factory as ff
import numpy as np

# np.random.seed(123)

x1 = np.random.randn(50)-2
x2 = np.random.randn(50)
x3 = np.random.randn(50)+2
x4 = np.random.randn(50)+4


fig= ff.create_distplot([x1,x2,x3,x4],['x1 group','x2 group','x3 group','x4 group'], bin_size=[1,2,3,4])

pyo.plot(fig)