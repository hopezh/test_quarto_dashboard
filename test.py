import polars as pl
import plotly.express as px
import plotly.graph_objects as go

# create df for solar farms
data_solar_farms = {
    "name"          : ["Setouchi Kirei", "Eurus Rokkasho", "Tomatoh Abira"],
    "capacity_mw"   : [235, 148, 111],
    "latitude"      : [34.6, 40.9, 42.7],
    "longitude"     : [134.1, 141.3, 141.7],
    "state"         : ["Okayama", "Aomori", "Hokkaido"],
    "city"          : ["Setouchi", "Rokkasho", "Abira"],
    "year_operation": [2018, 2015, 2015],
}
df_solar_farms = pl.DataFrame(data_solar_farms)

# create df for typhoon paths
data_typhoon = {
    'name'            : ['Lan',  'Lan',  'Lan',  'Guc',  'Guc',  'Guc'],
    'idx'             : [230701, 230702, 230703, 220301, 220302, 220303],
    'latitude'        : [31.1,   36.6,   41.0,   31.8,   36.6,   37.8],
    'longitude'       : [137.3,  133.0,  135.8,  128.4,  135.0,  142.2],
    'date_time'       : [
        '2022-08-07 00:00:00',
        '2022-08-07 06:00:00',
        '2022-08-07 12:00:00',
        '2023-06-06 18:00:00',
        '2023-06-07 00:00:00',
        '2023-06-07 06:00:00',
    ],
    'grade'           : [1, 3, 2, 4, 6, 5]
}
df_typhoon = pl.DataFrame(data_typhoon)

#| title: map of typhoon paths
fig_typhoon = px.line_mapbox(
    df_typhoon,
    lat='latitude',
    lon='longitude',
    color='name',
    # animation_frame='name',
)

fig_typhoon.update_layout(
    mapbox_style="carto-darkmatter",
    mapbox_center_lat=36,
    mapbox_center_lon=138,
    mapbox_zoom=3,
)

#| title: map solar farms
fig_solar_farms = go.Figure(
    go.Scattermapbox(
        lat = df_solar_farms['latitude'],
        lon = df_solar_farms['longitude'],
        mode = 'markers',
        marker = go.scattermapbox.Marker(
            size=df_solar_farms['capacity_mw']/10
        ),
    )
)

fig_solar_farms.update_layout(
    mapbox_style="carto-darkmatter",
    mapbox=dict(
        center=go.layout.mapbox.Center(
            lat=36,
            lon=138
        ),
        zoom=3
    ),
)

# add typhoon map to solar map
fig_solar_farms.add_trace(
    fig_typhoon.data[0]
)

fig_solar_farms.show()
