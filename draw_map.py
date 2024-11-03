import folium
import branca.colormap as cm
import pandas as pd


def draw_scatter_point_map(station_status, station_information) :
    percentage_filled = {
        j['station_id'] : j['num_docks_available'] / (j['num_docks_available'] + j['num_bikes_available'])
        for j in station_status if j['num_docks_available'] + j['num_bikes_available'] > 0
    }
    
    colormap = cm.LinearColormap(colors=["red", "green"], index=[0,1],vmin=0,vmax=1)

    m = folium.Map(location=(48.87929591733507, 2.3373600840568547), zoom_start=11)
    for _, station in station_information.iterrows():
        station = station.to_dict()
        station_id = station['station_id']
        if station_id in percentage_filled :
            folium.Circle(
                location=[station['lat'], station['lon']],
                radius=10,
                fill=True,
                color=colormap(percentage_filled[station_id]),
            ).add_to(m)

    return m

if __name__ == '__main__' :
    from download_data import get_station_information
    import json 

    station_information = pd.DataFrame(get_station_information())
    with open('data/station_status_2411030220.json') as f :
        station_status = json.load(f)
    my_map = draw_scatter_point_map(station_status, station_information)
    my_map.save("data/map.html")