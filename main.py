import geopandas as gpd
import geoplot as gplt
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# df = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv')
df = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Long_, df.Lat)
)
gdf = gdf[
    (gdf.Province_State != 'Guam') &
    (gdf.Province_State != 'American Samoa') &
    (gdf.Province_State != 'Northern Mariana Islands') &
    (gdf.Province_State != 'Virgin Islands') &
    # (gdf.Province_State != 'Hawaii') &
    # (gdf.Province_State != 'Alaska') &
    (gdf.Province_State != 'Puerto Rico') &
    (gdf.Province_State != 'Diamond Princess') &
    (gdf.Province_State != 'Grand Princess') &
    (gdf.Long_ < -40.)
    ]  #['Guam', 'American Samoa', 'Northern Mariana Islands', 'Virgin Islands']]

fig = plt.figure()
ax = fig.add_subplot(111)
from mpl_toolkits.axes_grid1 import make_axes_locatable
# divider = make_axes_locatable(ax)
# cax = divider.append_axes('right', size='5%', pad=0.1)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[world.name == 'United States of America']
world.boundary.plot(ax=ax, color='k')
gdf['difference'] = gdf['5/16/20'] - gdf['5/15/20']
# gdf = gdf[(gdf['difference']> 0.)]

# cities = gpd.read_file(gplt.datasets.get_path('usa_cities'))
gdf.plot(column='difference', ax=ax, legend=True, markersize=5, scheme='quantiles')
# gplt.cartogram(gdf, scale='difference', ax=ax)
# ax = gplt.polyplot
#     gdf, projection=gplt.crs.Orthographic(), figsize=(8,4)
# )
# ax.outline_path.set_visible(True)
#
# gplt.show()
plt.savefig('figure.png')
# mpld3.save_html(fig, 'figure.html')