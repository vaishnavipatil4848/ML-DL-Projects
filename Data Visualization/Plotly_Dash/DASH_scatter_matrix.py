import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
from dash.dependencies import Input,Output

df= pd.read_csv('CSV Files for Dash\\social_capital.csv')
df.drop(['Alt FIPS Code','FIPS Code','State Abbreviation'],axis=1,inplace=True)

#-----------------------------------------------------------------------------
app=dash.Dash(__name__)

app.layout=
