import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import os
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

df = pd.read_csv('complexsite.csv')
# img = io.imread('factorysite.png')
fig = make_subplots(1, 1)

app = dash.Dash(__name__)
server = app.server

GITHUB_LINK = os.environ.get(
    "GITHUB_LINK",
    "https://github.com/evileyelivelx/dashapp_microbiology",
)

layout = go.Layout(
    showlegend=True,
    autosize=True,
    xaxis=go.XAxis(showticklabels=False),
    yaxis=go.YAxis(showticklabels=False),
    margin=dict(l=10, r=10, b=50, t=20),
    images=[dict(
        source="assets/factorysite.png",
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
        html.Div([
            html.H1(children='Dash - Site Plan & Line Chart',
                    className='nine columns'),
            html.Img(
                src='assets/cawthronlogo.png',
                className='three columns',
                style={
                    'height': '16%',
                    'width': '16%',
                    'float': 'right',
                    'position': 'relative',
                    'padding-top': 12,
                    'padding-right': 0
                }
            ),

            # html.Div(children='''
            #         Data visualization for a site plan with mock data.
            # ''',
            #          className='nine columns')
            html.Div([
                html.H6("This Dash app is a simple demonstration of the result performance of the production facility in XXX company. "
                       "The dataset consists of 120 observations in the last six months, representing the positive number from "
                       "individual facility. Drag the slider to view the number of positive result in each facility over the last six months, the larger "
                       "circle means the more positive result has been detected. The right side the line chart is representing the trend "
                       "for each site or facility from January 2018 to June 2018."),
            ], className='six columns')
        ], className="row"),

        # Selectors
        html.Div([
            html.Div([
               dcc.Slider(
                   id='dateslider',
                   min=df['Number'].min(),
                   max=df['Number'].max(),
                   value=df['Number'].min(),
                   # marks={str(num): str(num) for num in df['Number'].unique()},
                   marks={
                       0: "2018-Jan",
                       2: "2018-Feb",
                       4: "2018-Mar",
                       6: "2018-Apr",
                       8: "2018-May",
                       10: "2018-Jun"
                   },
                   step=None
               )
            ], className='six columns'),

            html.Div([
                html.P('Select Facility:'),
                dcc.Dropdown(
                    id='site',
                    options=[{'label': str(item),
                              'value': str(item)}
                             for item in set(df['Location'])],
                    multi=True,
                    value=list(set(df['Location']))
                )
            ], className='five columns',
                style={'margin-top': '10'})
        ], className='row'),

        # Site plan + Line chart
        html.Div([
            html.Div([
                dcc.Graph(id='siteplan',
                          animate=True,
                          config={'displayModeBar': True},
                          style={'background': '#0a0000', 'padding-bottom': '10px',
                                 'padding-left': '10px', 'padding-right': '20px',
                                 'height': '60vh', "padding-top": '50px'})
            ], className='six columns'),

            html.Div([
                dcc.Graph(id='linechart',
                          style={'background': '#0a0000', 'padding-bottom': '10px',
                                 'padding-left': '10px', 'padding-right': '20px',
                                 'height': '60vh', "padding-top": '50px'})
            ], className='six columns')
        ]),

        html.Div([
            html.Div([
                html.H6("For more information please contact: \ "
                        "Steven.Liu@cawthron.org.nz"),
            ], className='nine columns'),

            html.Div([
                html.A(
                    "View on Steven Liu's GitHub",
                    href=GITHUB_LINK
                )
            ], className='nine columns')
        ])
    ])
])

@app.callback(
    Output('siteplan', 'figure'),
    [Input('dateslider', 'value')]
)
def update_figure(selected_num):
    filtered_df = df[df['Number'] == selected_num]
    traces=[]
    # fig.add_trace(go.Image(z=img), 1, 1)

    for i in filtered_df['Location'].unique():
        df_location = filtered_df[filtered_df['Location'] == i]
        traces.append(dict(
            x=df_location['Lat'],
            y=df_location['Lon'],
            text=df_location['Result'],
            mode='markers',
            marker={
                'size': df_location['Result']*4,
                'color': df_location['Color']
            },
            name=i,
        )
        )

    return {
        'data': traces,
        'layout': layout
    }

@app.callback(
    Output('linechart', 'figure'),
    [Input('site', 'value')]
)
def build_linechart(site):
    site_df = df[df['Location'].isin(site)]
    fig = px.line(site_df, x='Date', y='Result', color='Location')
    fig.update_layout(yaxis={'title': 'Positive Result'},
                      title={'text': 'Data analysis in different facilities'})

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
