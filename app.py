import plotly.express as px
import plotly.graph_objects as go
from skimage import io
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# img = io.imread('assets/example.png')
df = pd.read_csv('sitedata.csv')


# fig.update_layout(coloraxis_showscale=True)
# fig.show()

# fig.add_trace(go.Scatter(x=[120], y=[70], text='polo', marker=dict(color='purple', size=30)))

# app = dash.Dash(__name__)
# server = app.server
#
# app.layout = html.Div([
#     html.H2('A Mock Data Visualization for Site Processing Facility'),
#     dcc.Graph(id='site'),
#     dcc.Slider(
#         id='year-slider',
#         marks={
#             0: 'Jan 2018',
#             2: 'Feb 2018',
#             4: 'Mar 2018',
#             6: 'Apr 2018',
#             8: 'May 2018',
#             10: 'June 2018'
#         },
#         min=0,
#         max=10,
#         value=4,
#         step=None,
#     )
# ])
#
#
# @app.callback(
#     Output('site', 'figure'),
#     [Input('year-slider', 'value')]
# )
# def update_figure(selected_date):
#     filter_data = df[df['Number'] == selected_date]
#     traces = []
#     for i in filter_data['Location'].unique():
#         fig.add_trace(go.Scatter(x=filter_data['Lat'], y=filter_data['Lon'],
#                                                     text=filter_data['Location'],
#                                                     marker=dict(color=filter_data['Color'],
#                                                                 size=filter_data['Number'])))
#
#     return {
#         'data': traces,
#
#     }
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H2(children='Test'),
    html.Div([
        dcc.Graph(
            id='sitemap'
        ),
        dcc.Slider(
            id='slider',
            min=0,
            max=10,
            value=3,
            marks={0, 2, 4, 6, 8, 10}
        )
    ])
])

@app.callback(
    Output('sitemap', 'figure'),
    [Input('slider', 'value')]
)

def update_figure(selected_number):
    filtered_df = df[df['Number'] == selected_number]
    traces = []
    for i in filtered_df['Location'].unique():
        df_location = filtered_df[filtered_df['Location'] == i]
        # fig = px.imshow(img)
        new_trace = go.Scatter(
            x=[df_location['Lat']],
            y=[df_location['Lon']],
            marker=dict(color=df_location['Color'], size=df_location['Result']),


        )
        # traces.append(fig)
        traces.append(new_trace)

    layout_site = go.Layout(

    )

    return {
        'data': traces,
        'layout': layout_site
    }

if __name__ == '__main__':
    app.run_server(debug=True)


























