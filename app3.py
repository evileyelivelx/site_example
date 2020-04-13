import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from skimage import io
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

df = pd.read_csv('sitedata.csv')
img = io.imread('assets/example.png')
fig = make_subplots(1, 1)

app = dash.Dash(__name__)
server = app.server

layout = go.Layout(
    showlegend=True,
    autosize=False,
    title=dict(text='Result show on the facility site', font=dict(size=20, color='Black')),
    margin=dict(l=0, r=0, b=50, t=80),
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

    # dcc.Graph(id='sitemap', style={
    #     'background-image': 'url(https://images.unsplash.com/photo-1581293738298-451cd74b0b45?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=935&q=80)'}),
    dcc.Graph(id='sitemap'),
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
    ),

], className='six columns')


@app.callback(
    Output('sitemap', 'figure'),
    [Input('dateslider', 'value')]
)
def update_figure(selected_num):
    filtered_df = df[df['Number'] == selected_num]
    traces = []
    fig.add_trace(go.Image(z=img), 1, 1)

    for i in filtered_df['Location'].unique():
        df_location = filtered_df[filtered_df['Location'] == i]
        traces.append(dict(
            x=df_location['Lat'],
            y=df_location['Lon'],
            text=df_location['Location'],
            mode='markers',
            marker={
                'size': df_location['Result'] * 5,
                'color': df_location['Color']
            },
            name=i,
        )
        ),

    return {
        'data': traces,
        'layout': layout
    }


if __name__ == '__main__':
    app.run_server(debug=True)
