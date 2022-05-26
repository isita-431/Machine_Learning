# import packages
import dash
import  dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# load the "wind_speed_laurel_nebraska.csv" file

dataset= pd.read_csv('wind_speed_laurel_nebraska.csv')

# launch the application
app = dash.Dash()


# create a line plot using the 'Time' and '10 Min Sampled Avg'
app.layout = html.Div([html.H1('Dash exercise solution'), dcc.Graph(id='scatterplot',
                                                                          figure={'data':[go.Scatter(
                                                                              x=dataset['Time'],
                                                                              y=dataset['10 Min Sampled Avg'] ,mode='lines',

                                                                          ) ],
                                                                              'layout': go.Layout(title='line plot',
                                                                                                  xaxis={'title':'Time'},
                                                                                                  yaxis ={'title':'10 Min Sampled Avg'}),

                                                                          }) ,])



# run the server
if __name__ =='__main__':
    app.run_server()
