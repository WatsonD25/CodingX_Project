import folium

# mapr加legend
# https://stackoverflow.com/questions/37466683/create-a-legend-on-a-folium-map
# https://nbviewer.jupyter.org/gist/talbertc-usgs/18f8901fc98f109f2b71156cf3ac81cd
# https://jingwen-z.github.io/how-to-draw-a-map-with-folium-module-in-python/

# from folium import plugins

main_map = folium.Map(location=[23.000909, 120.223148],zoom_start=12)
tooltip='點擊獲取更多資訊'
popup=folium.Popup(html='<b>台南市東區大學路1號</b>',max_width=200)
folium.Marker(location=[22.996319990137735,120.21953003491251],tooktip=tooltip,popup=popup,icon=folium.Icon(color='red')).add_to(main_map)
#flood
flood_tainan_6h_150mm=folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood1_6150.json",
    name="6小時內下雨150mm之淹水區域",
    style_function=lambda x : {"stroke":False,"fillColor":"#ffd600","fillOpacity":0.75}
).add_to(main_map)
flood_tainan_6h_150mm.add_child(folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood2_6150.json",
    name="6小時內下雨150mm之淹水區域",
    style_function=lambda x : {"stroke":False,"fillColor":"#ffab00","fillOpacity":0.75}
))
flood_tainan_6h_150mm.add_child(folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood3_6150.json",
    name="6小時內下雨150mm之淹水區域",
    style_function=lambda x : {"stroke":False,"fillColor":"#ff6d00","fillOpacity":0.75}
))
flood_tainan_6h_150mm.add_child(folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood4_6150.json",
    name="6小時內下雨150mm之淹水區域",
    style_function=lambda x : {"stroke":False,"fillColor":"#dd2c00","fillOpacity":0.75}
))


folium.LayerControl().add_to(main_map)
main_map.save("map_for_flood_tainan_6h_150mm.html")


