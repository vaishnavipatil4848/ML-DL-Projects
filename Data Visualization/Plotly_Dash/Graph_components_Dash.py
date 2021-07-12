import pandas as pd
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.express as px

df=px.data.gapminder()

external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout=html.Div([
    dcc.Dropdown(id='drop',value=['Germany','Brazil'],multi=True, 
    options=[{'label':x,'value':x}for x in df.country.unique()]),

    html.Div([
        dcc.Graph(id='piegraph',figure={},className='six columns'),
        dcc.Graph(id='linegraph',figure={},
        config={
            'staticPlot':False,
            'scrollZoom':True,
            'doubleClick':'reset',
            'showTips':True,
            'displayModeBar':True,
            'watermark':True
        }, 
        className='six columns'
        )
    ])
])

@app.callback(
    Output(component_id='linegraph',component_property='figure'),
    Input(component_id='drop',component_property='value'),
)

def update_graph(country_chosen):
    dff=df[df.country.isin(country_chosen)]
    fig=px.line(data_frame=dff,x='year',y='gdpPercap',color='country',
    custom_data=['country','continent','lifeExp','pop'])
    fig.update_traces(mode='lines+markers')
    return fig

@app.callback(
    Output(component_id='piegraph',component_property='figure'),
    Input(component_id='linegraph',component_property='hoverData'),
    Input(component_id='linegraph',component_property='clickData'),
    Input(component_id='linegraph',component_property='selectedData'),
    Input(component_id='drop',component_property='value')
)

def update_graph(hov_data,click_data,slct_data,country_chosen):
    if hov_data is None:
        dff2=df[df.country.isin(country_chosen)]
        dff2=dff2[dff2.year==1952]
        print(dff2)
        fig2=px.pie(data_frame=dff2,values='pop',names='country',title='Population for 1952')
        return fig2
    else:
        print(f'hover Data:{hov_data}')
        print(f'click data:{click_data}')
        print(f'selected data:{slct_data}')
        dff2=df[df.country.isin(country_chosen)]
        hov_year=hov_data['points'][0]['x']
        dff2=dff2[dff2.year==hov_year]
        fig2=px.pie(data_frame=dff2,values='pop',names='country', title=f'Population for:{hov_year}')
        return fig2


if __name__=='__main__':
    app.run_server(debug=True)