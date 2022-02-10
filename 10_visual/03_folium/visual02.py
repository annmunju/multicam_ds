import folium

location = [37.56392875136698, 127.05444464044996]
my_loc = folium.Map(location=location, zoom_start=18)
folium.Marker(location, popup=folium.Popup('문주네 집', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')