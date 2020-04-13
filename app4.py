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

# app = dash.Dash(__name__)
# server = app.server
#
#
# app.layout = html.Div([
#     # html.Img(src='assets/example.png'),
#     dcc.Graph(id='sitemap'),
#     dcc.Slider(
#         id='dateslider',
#         min=df['Number'].min(),
#         max=df['Number'].max(),
#         value=df['Number'].min(),
#         marks={str(num): str(num) for num in df['Number'].unique()},
#         step=None
#     )
# ])
#
# @app.callback(
#     Output('sitemap', 'figure'),
#     [Input('dateslider', 'value')]
# )
#
# def update_figure(selected_num):
#     filtered_df = df[df['Number'] == selected_num]
#     traces = []
#
#     for i in filtered_df['Location'].unique():
#         df_location = filtered_df[filtered_df['Location'] == i]
#
#         traces.append(go.Scatter(
#             x=df_location['Lat'],
#             y=df_location['Lon'],
#             marker=dict(color=df_location['Color'], size=df_location['Result']*10)
#         ))
#         fig.add_trace(go.Image(z=img), 1, 1)
#         fig.add_trace(traces)
#         fig.show()
#
#
#     return {
#         'data': traces,
#         'layout': dict(
#             xaxis={'type': 'log', 'title': 'Test Sample'},
#             yaxis={'title': " "}
#         )
#     }
#
#
# if __name__ == '__main__':
#     app.run_server(debug=False)

for color in df['Color']:
    fig.add_trace(go.Scatter(
        x=df['Lat'],
        y=df['Lon'],
        marker=dict(color=df['Color'], size=df['Result']*20)
    ))
    fig.update_layout(height=400)
    fig.show()











