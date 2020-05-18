import geopandas as gpd
import geoplot as gplt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Long_, df.Lat)
)
gdf = gdf[
    (gdf.Province_State != 'Guam') &
    (gdf.Province_State != 'American Samoa') &
    (gdf.Province_State != 'Northern Mariana Islands') &
    (gdf.Province_State != 'Virgin Islands') &
    (gdf.Province_State != 'Hawaii') &
    (gdf.Province_State != 'Alaska') &
    (gdf.Province_State != 'Puerto Rico') &
    (gdf.Province_State != 'Diamond Princess') &
    (gdf.Province_State != 'Grand Princess') &
    (gdf.Long_ < -40.)
    ]  #['Guam', 'American Samoa', 'Northern Mariana Islands', 'Virgin Islands']]

gdf.boundary.plot()
fig = plt.figure()
ax = fig.add_subplot(111)
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.1)

gdf.plot(column='5/15/20', ax=ax, legend=True)
# ax = gplt.polyplot(
#     gdf, projection=gplt.crs.Orthographic(), figsize=(8,4)
# )
# ax.outline_path.set_visible(True)
#
# gplt.show()
plt.savefig('figure.png')