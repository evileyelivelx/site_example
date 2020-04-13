import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from skimage import io
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

df = pd.read_csv('sitedata2.csv')
img = io.imread('assets/example.png')
fig = make_subplots(1, 1)

app = dash.Dash(__name__)
server = app.server

layout = go.Layout(
    showlegend=True,
    autosize=True,
    xaxis=go.XAxis(showticklabels=False),
    yaxis=go.YAxis(showticklabels=False),
    # title=dict(text='', font=dict(size=20, color='Black')),
    margin=dict(l=10, r=10, b=50, t=20),
    images=[dict(
        source="assets/example.png",
        # positon='middle center',
        xref="x",
        yref="y",
        x=0.75,
        y=35,
        sizex=50,
        sizey=50,
        xanchor='left',
        yanchor='top',
        sizing="contain",
        opacity=1,
        layer="below",

    )])

app.layout = html.Div([
        html.Div([
            html.Label(['Choose 3 facilities to compare: '],
                       style={'font-weight': ' bold', "text-align": 'center'}),

            dcc.Dropdown(id='facility_one',
                         options=[{'label': x, 'value': x} for x in df.sort_values('Location')['Location'].unique()],
                         value='site1',
                         multi=False,
                         disabled=False,
                         clearable=False,
                         searchable=True,
                         placeholder='Choose a site facility...',
                         className='form-dropdown',
                         style={'width': '90%'},
                         persistence='string',
                         persistence_type='memory'
                         ),

            dcc.Dropdown(id='facility_two',
                         options=[{'label': x, 'value': x} for x in df.sort_values('Location')['Location'].unique()],
                         value='site2',
                         multi=False,
                         clearable=False,
                         persistence='string',
                         ),

            dcc.Dropdown(id='facility_three',
                         options=[{'label': x, 'value': x} for x in df.sort_values('Location')['Location'].unique()],
                         value='site3',
                         multi=False,
                         clearable=False,
                         persistence='string',
                         ),

        ], className='three columns'),

        html.Div([
            dcc.Graph(id='barchart')
        ], className='seven columns')

    ])


@app.callback(
    Output('barchart', 'figure'),
    [Input('facility_one', 'value'),
     Input('facility_two', 'value'),
     Input('facility_three', 'value')]
)
def build_graph(site1, site2, site3):
    filtered_site = df[(df['Location'] == site1) |
                       (df['Location'] == site2) |
                       (df['Location'] == site3)]

    fig = px.line(filtered_site, x='Date', y='Result', color='Color', height=600)
    fig.update_layout(yaxis={'title': 'Positive Result'},
                      title={'text': 'Data analysis in different facilities'})

    return fig


if __name__ == '__main__':
    app.run_server(debug=False)
