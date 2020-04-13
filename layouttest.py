# This is an example from the Japanese guy online about how to set up layout


import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd

from plotly import graph_objs as go
from plotly.graph_objs import *
from dash.dependencies import Input, Output, State

layout_table = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=35,
        b=35,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
)
layout_table['font-size'] = '12'
layout_table['margin-top'] = '20'

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1(children="Maps and Tables", className='nine columns'),
            html.Img(
                src="http://xxx.png",
                className='three columns',
                style={
                    'height': '16%',
                    'width': '16%',
                    'float': 'right',
                    'position': 'relative',
                    'padding-top': 12,
                    'padding-right': 0
                },
            ),
            html.Div(children='''
            Dash Tutorial video 04: Working with tables and maps''',
                     className='nine columns')
        ], className='row'),

        # Selectors
        html.Div([
            html.Div([
                html.P('Choose Boroughs'),
                dcc.Checklist(
                    id='boroughs',
                    options=[
                        {'label': 'Manhattan', 'value': 'MN'},
                        {'label': 'Bronx', 'value': 'BX'},
                        {'label': 'Queens', 'value': 'QU'},
                        {'label': 'Brooklyn', 'value': 'BK'},
                        {'label': 'Staten Island', 'value': 'SI'}
                    ],
                    values=['MN', 'BX', "QU", "BK", "SI"],
                    labelStyle={'display': 'inline-block'}
                )
            ],
                className='six columns',
                style={'margin-top': '10'}
            ),

            html.Div([
                html.P('Type: '),
                dcc.Dropdown(
                    id='type',
                    options=[{
                        'label': str(item), 'value': str(item)
                    } for item in set(map_data['Type'])],
                    multi=True,
                    value=list(set(map_data['Type']))
                )
            ],
                className='six columns',
                style={'margin-top': '10'}
            )
        ], className='row'),

        # Map Table Histo
        html.Div([
            html.Div([
                dcc.Graph(
                    id='',
                    animate=True,
                    style={'margin-top': '20'}
                )
            ], className='six columns'),

            html.Div([
                dt.Datable(
                    rows="",
                )
            ],
                style="",
                className='six columns'),

            html.Div([
                dcc.Graph(
                    id='bar-graph'
                )
            ], className='twelve columns'),

            html.Div(
                [
                    html.P('Developed by Adriano M. Yoshino - ', style={'display': 'inline'}),
                    html.A('amyoshino@nyu.edu', href='mailto:amyoshino@nyu.edu')
                ], className="twelve columns",
                style={'fontSize': 18, 'padding-top': 20}
            )

        ], className='row')

    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
