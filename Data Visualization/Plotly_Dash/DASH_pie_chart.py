import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

df=pd.read_csv('CSV Files for Dash\\Urban_park_Ranger_Animal_Condition_Response.csv')

#you need to include __name__in your constructor if you
#plan to use a custom css or Javascript in your Dash apps.

app=dash.Dash(__name__)

#_________________________________________________________________

#App Layout:
app.layout=html.Div([
    html.H1("Animal Analysis in USA ",style={'text-align':'center','background-color':'coral','font-family':'Monospace','font-size':'xxlarge'}),
    dcc.Dropdown(
        id="Options",
        options=[
            {'label':'Action Taken by Ranger','value':'Final ranger action'},
            {'label':'Age','value':'Age'},
            {'label':'Animal Health','value':'Animal Condition'},
            {'label':'Borough','value':'Borough'},
            {'label':'Species','value':'Animal Class'},
            {'label':'Species Status','value':'Species Status'}
        ],
        value='Animal Class',
        multi=False, 
        clearable=False,
        style={'width':'50%','height':'60%'}
    ), 
    html.Div([
        dcc.Graph(id="my_piechart",style={'margin':'40px 40px 200px 250px'})
    ])
    ])

#___________________________________________________________________________________________
#App Callback(connecting graph to dash components)
@app.callback(
    Output(component_id='my_piechart',component_property='figure'),
    [Input(component_id='Options',component_property='value')]

)

def update_graph(options):
    dff=df

    piechart=px.pie(
        data_frame=dff,
        names=options,
        hole=.3,
        template='plotly_dark'
    )
    return(piechart)
#_____________________________________________________________________________________________

if __name__=='__main__':
    app.run_server(debug=True)

    

