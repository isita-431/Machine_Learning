import dash
import  dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd


dataset = pd.read_csv('headbrain1.csv')
print(dataset.head())

app= dash.Dash()

app.layout = html.Div([html.H1('Scatter plot'), dcc.Graph(id='scatterplot 1',
                                                          figure={'data':[go.Scatter(x=dataset['Head Size(cm^3)'],y= dataset['Brain Weight(grams)'],mode='markers',
                                                                                     marker={'size':10,'color':'red','symbol':'circle'})],
                                                                          'layout': go.Layout(title='Scatterplot 1',
                                                                                              xaxis={'title':'Head size'},

                                                                                           yaxis={'title':'Brain weight'})}),
                       dcc.Graph(id='scatterplot 2',
                                 figure={'data':[go.Scatter(x=dataset['Head Size(cm^3)'],y= dataset['Brain Weight(grams)'],mode='markers',
                                                            marker={'size':10,'color':'blue','symbol':'pentagon'})],
                                         'layout': go.Layout(title='Scatterplot 2',
                                                             xaxis={'title':'Head size'},

                                                             yaxis={'title':'Brain weight'})}) ])

if __name__ =='__main__':
    app.run_server()