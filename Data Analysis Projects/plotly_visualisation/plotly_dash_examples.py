# import the packages
import dash
import dash_core_components as dcc
import dash_html_components as html



# html - head and body - div -h1
# <h1 style= ''> </h1>

app= dash.Dash()

colors = {'backgroud':'#FFFFCC','text':'660033'}

app.layout = html.Div(children=[html.H1('This is a demo dash app',style={'textAlign':'center','color':colors['text']}),
                                dcc.Graph(id='example',
                                          figure ={'data':[{'x':[10,20,30],
                                                             'y':[1,2,3],'type':'bar','name':'teamA'},
                                                           {'x':[50,60,70],
                                                            'y':[4,5,6],'type':'bar','name':'teamB'}],
                                                'layout':{'title':'A simple bar plot',
                                                          'plot_bgcolor':colors['backgroud'],
                                                          'font':{'color':colors['text']}}})],
                      style={'backgroundColor':colors['backgroud']})




if __name__=='__main__':
    app.run_server()