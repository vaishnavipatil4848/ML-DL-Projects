import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px
import plotly.graph_objs as go
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output

df=pd.read_csv('CSV Files for Dash\\Urban_park_Ranger_Animal_Condition_Response.csv')
df=df[(df['# of Animals']>0) & (df['Age']!='Multiple')]
df['Month of Initial call']=pd.to_datetime(df['Date and Time of initial call'])
df['Month of Initial call']=df['Month of Initial call'].dt.strftime('%m')
df['Amount of animals']=df['# of Animals']
df['Time spent on Site(hours)']=df['Duration of Response']
#-----------------------------------------------------------------------------------
app=dash.Dash(__name__)

#-----------------------------------------------------------------------------------
app.layout=html.Div([
    html.Div([
        html.Pre(children='NYC Calls for Animal Rescue',
        style={'color':'black','font-family':'Serif','font-size':'150%','text-align':'center'})

    ]),

    html.Div([
        html.Label(['X axis for comparison'],
        style={'font-family':'San Serif','color':'black','font-size':'50%'}),
        dcc.RadioItems(
            id='xaxis_ritem',
            options=[
                {'label':'Month Call Made','value':'Month of Initial call'},
                {'label':'Animal Health','value':'Animal Condition'},
            ],
            value='Animal Condition',
            style={'width':'50%'}
        ),
    ]),

    html.Div([
        html.Br(),
        html.Label(['Y axis for comparison'],
        style={'color':'black','font-family':'San Serif','font-size':'40%'}),
        dcc.RadioItems(
            id='yaxis_ritem',
            options=[
                {'label':'Time Spent on Site','value':'Time spent on Site(hours)'},
                {'label':'Amount of Animals','value':'Amount of animals'},
            ],
            value='Time spent on Site(hours)',
            style={'width':'50%'}
        ),
    ]),
    html.Div([
        dcc.Graph(id="bargraph")
    ]),

])
#---------------------------------------------------------------------------------
@app.callback(
    Output(component_id='bargraph',component_property='figure'),
    [Input(component_id='xaxis_ritem',component_property='value'),
    Input(component_id='yaxis_ritem',component_property='value')]
)

def update_graph(xaxis,yaxis):
    dff=df
    bar_chart=px.bar(
        data_frame=dff,
        x=xaxis,
        y=yaxis,
        title=yaxis+': by' +xaxis,
        #color='Borough',
        facet_col='Borough',
        #barmode='group',
        
    )
    return(bar_chart)

if __name__=='__main__':
    app.run_server(debug=True)