# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from skimage import io
# import pandas as pd
# import dash
# import dash_html_components as html
# import dash_core_components as dcc
# from dash.dependencies import Input, Output
#
# df = pd.read_csv('sitedata2.csv')
# img = io.imread('assets/example.png')
# fig = make_subplots(1, 1)
#
# app = dash.Dash(__name__)
# server = app.server
#
# layout = go.Layout(
#     showlegend=True,
#     autosize=True,
#     xaxis=go.XAxis(showticklabels=False),
#     yaxis=go.YAxis(showticklabels=False),
#     # title=dict(text='', font=dict(size=20, color='Black')),
#     margin=dict(l=10, r=10, b=50, t=20),
#     images=[dict(
#         source="assets/example.png",
#         # positon='middle center',
#         xref="x",
#         yref="y",
#         x=0.75,
#         y=35,
#         sizex=50,
#         sizey=50,
#         xanchor='left',
#         yanchor='top',
#         sizing="contain",
#         opacity=1,
#         layer="below",
#
#     )])
#
# app.layout = html.Div([
#
#     # dcc.Graph(id='sitemap', style={
#     #     'background-image': 'url(https://images.unsplash.com/photo-1581293738298-451cd74b0b45?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=935&q=80)'}),
#     html.Div([
#         html.H2(children='Dash - '),
#         html.H3(children='Data visualization for facility site from Jan 2018 to June 2018',
#                 className='six columns'),
#         html.Img(
#             src='assets/cawthronlogo.png',
#             className='three columns',
#             style={
#                 'height': '15%',
#                 'width': '15%',
#                 'float': 'right',
#                 'position': 'relative',
#                 'padding-top': 8,
#                 'padding-right': 0
#             }
#         ),
#
#         html.Div([
#
#             dcc.Graph(id='sitemap', config={'displayModeBar': True},
#                       style={'background': '#0a0000', 'padding-bottom': '10px',
#                              'padding-left': '10px', 'padding-right': '20px',
#                              'height': '60vh', "padding-top": '50px'},
#                       className='six columns'),
#
#             # dcc.Slider(
#             #     id='dateslider',
#             #     min=df['Number'].min(),
#             #     max=df['Number'].max(),
#             #     value=df['Number'].min(),
#             #     # marks={str(num): str(num) for num in df['Number'].unique()},
#             #     marks={
#             #         0: "2018-Jan",
#             #         2: "2018-Feb",
#             #         4: "2018-Mar",
#             #         6: "2018-Apr",
#             #         8: "2018-May",
#             #         10: "2018-Jun"
#             #     },
#             #     step=None
#             # ),
#             html.Div([
#                 html.P('Type:'),
#                 dcc.Dropdown(
#                     id='site',
#                     options=[{'label': str(item),
#                               'value': str(item)}
#                              for item in set(df['Location'])],
#                     multi=True,
#                     value=list(set(df['Location']))
#                 )
#             ], className='six columns',
#                 style={'margin-top': '10'})
#
#         ], className='row'),
#
#         html.Div([
#             html.Div([
#                 dcc.Slider(
#                     id='dateslider',
#                     min=df['Number'].min(),
#                     max=df['Number'].max(),
#                     value=df['Number'].min(),
#                     # marks={str(num): str(num) for num in df['Number'].unique()},
#                     marks={
#                         0: "2018-Jan",
#                         2: "2018-Feb",
#                         4: "2018-Mar",
#                         6: "2018-Apr",
#                         8: "2018-May",
#                         10: "2018-Jun"
#                     },
#                     step=None
#                 ),
#             ], className='six columns'),
#
#             html.Div([
#                 dcc.Graph(id='barchart')
#             ], className='six columns')
#         ], className='row'),
#     ]),
#
# ])
#
#
# @app.callback(
#     Output('sitemap', 'figure'),
#     [Input('dateslider', 'value')]
# )
# def update_figure(selected_num):
#     filtered_df = df[df['Number'] == selected_num]
#     traces = []
#     fig.add_trace(go.Image(z=img), 1, 1)
#
#     for i in filtered_df['Location'].unique():
#         df_location = filtered_df[filtered_df['Location'] == i]
#         traces.append(dict(
#             x=df_location['Lat'],
#             y=df_location['Lon'],
#             text=df_location['Result'],
#             mode='markers',
#             marker={
#                 'size': df_location['Result'] * 5,
#                 'color': df_location['Color']
#             },
#             name=i,
#         )
#         ),
#
#     return {
#         'data': traces,
#         'layout': layout
#     }
#
#
# @app.callback(
#     Output('barchart', 'figure'),
#     [Input('site', 'value')]
# )
# # def build_graph(site1, site2, site3):
# #     filtered_site = df[(df['Location'] == site1) |
# #                        (df['Location'] == site2) |
# #                        (df['Location'] == site3)]
# #
# #     fig = px.line(filtered_site, x='Date', y='Result', color='Location', height=600)
# #     fig.update_layout(yaxis={'title': 'Positive Result'},
# #                       title={'text': 'Data analysis in different facilities'})
# #
# #     return fig
# def build_linechart(site):
#     site_df = df[df['Location'].isin(site)]
#     fig = px.line(site_df, x='Date', y='Result', color='Location')
#     fig.update_layout(yaxis={'title': 'Positive Result'},
#                       title={'text': 'Data analysis in different facilities'})
#
#     return fig
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
