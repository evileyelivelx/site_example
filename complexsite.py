import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
from skimage import io
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

df = pd.read_csv('complexsite.csv')
img = io.imread('assets/factorysite.png')
fig = make_subplots(1, 1)

app = dash.Dash(__name__)
server = app.server

layout = go.Layout(
    showlegend=True,
    autosize=True,
    xaxis=go.XAxis(showticklabels=False),
    yaxis=go.YAxis(showticklabels=False),
    margin=dict(l=10, r=10, b=50, t=20),
    # image=

)

app.layout = html.Div([
    html.Div([
        html.H2(children='Dash - '),
        html.H3(children='Data visualization for facility site from Jan 2018 to June 2018',
                className='six columns'),
        # html.Img()
        html.Div([

            dcc.Graph(id='sitemap', config={'displayModeBar': True},
                      style={'background': '#0a0000', 'padding-bottom': '10px',
                             'padding-left': '10px', 'padding-right': '20px',
                             'height': '60vh', "padding-top": '50px'}),
            # dcc.Slider(
            #     id='dateslider',
            #     min=df['Number'].min(),
            #     max=df['Number'].max(),
            #     value=df['Number'].min(),
            #     # marks={str(num): str(num) for num in df['Number'].unique()},
            #     marks={
            #         0: "2018-Jan",
            #         2: "2018-Feb",
            #         4: "2018-Mar",
            #         6: "2018-Apr",
            #         8: "2018-May",
            #         10: "2018-Jun"
            #     },
            #     step=None
            # ),
        ], className='seven columns'),

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

        ], className='five columns'),

        html.Div([
            dcc.Graph(id='barchart')
        ], className='seven columns')

    ]),

])


@app.callback(
    Output('sitemap', 'figure'),
    # [Input('dateslider', 'value')]
)
def update_figure(select_num):
    filtered_df = df[df['Number'] == select_num]

    for i in filtered_df['Location'].unique():
        df_location = filtered_df[filtered_df['Location'] == i]
        fig = px.scatter(df_location, x='Lat', y='Lon', animation_frame='Date',
                         size='Result', color='Color')
        fig.add_layout_image(
            dict(
                source=Image.open('factorysite.png'),
                xref='x',
                yref='y',
                x=0,
                y=35,
                sizex=40,
                sizey=40,
                sizing='contain',
                opacity=0.9,
                layout='below'
            )
        )

        return fig

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

    fig2 = px.line(filtered_site, x='Date', y='Result', color='Location', height=600)
    fig2.update_layout(yaxis={'title': 'Positive Result'},
                      title={'text': 'Data analysis in different facilities'})

    return fig2


if __name__ == '__main__':
    app.run_server(debug=True)