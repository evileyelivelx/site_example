# https://plotly.com/python/images/#add-a-background-image
# Using px to make site plan map
from PIL import Image
import pandas as pd
import plotly
import plotly.express as px
from skimage import io


df = pd.read_csv('sitedata3.csv')
img = io.imread('assets/example.png')

fig = px.scatter(df, x="Lat", y="Lon", animation_frame="Date", size='Result', color='Color')
fig.add_layout_image(
    dict(
        # source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        source=Image.open("example.png"),
        # source="https://cdn.touchbistro.com/wp-content/uploads/2019/07/28-03-kitchen-floorplan.jpg",
        xref="x",
        yref="y",
        x=0,
        y=3,
        sizex=2,
        sizey=2,
        sizing="contain",
        opacity=0.9,
        layer="below")

)
fig.update_layout()

fig.show()
