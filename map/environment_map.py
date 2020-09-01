import folium
# from folium import plugins

main_map = folium.Map(location=[23.000909, 120.223148],zoom_start=12)


# 將地圖訂位到user的位置
# plugins.LocateControl(auto_start=True).add_to(main_map)

'''
#test
a=folium.GeoJson(
    "test_json_1.json",
    name='geojson',
    style_function=lambda x : {"stroke":False,"fillColor":"red","fillOpacity":0.5}
).add_to(main_map)

#用add_child可以控制合併圖層

a.add_child(folium.GeoJson(
    "test_json_2.json",
    name='geoj',
    style_function=lambda x : {"stroke":False,"fillColor":"blue","fillOpacity":0.5}
))
'''


#soil
soil=folium.GeoJson(
    "geojson_format_green_tainan.json",
    name="土壤液化",
    style_function=lambda x : {"stroke":False,"fillColor":"green","fillOpacity":0.7}
).add_to(main_map)
soil.add_child(folium.GeoJson(
    "geojson_format_yellow_tainan.json",
    name="土壤液化",
    style_function=lambda x : {"stroke":False,"fillColor":"yellow","fillOpacity":0.7}
))
soil.add_child(folium.GeoJson(
    "geojson_format_red_tainan.json",
    name="土壤液化",
    style_function=lambda x : {"stroke":False,"fillColor":"red","fillOpacity":0.7}
))

#flood
flood_tainan_6h_150mm=folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood1_6150.json",
    name="flood_tainan_6h_150mm",
    style_function=lambda x : {"stroke":False,"fillColor":"#ffd600","fillOpacity":0.75}
).add_to(main_map)
flood_tainan_6h_150mm.add_child(folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood2_6150.json",
    name="flood_tainan_6h_150mm",
    style_function=lambda x : {"stroke":False,"fillColor":"#ffab00","fillOpacity":0.75}
))
flood_tainan_6h_150mm.add_child(folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood3_6150.json",
    name="flood_tainan_6h_150mm",
    style_function=lambda x : {"stroke":False,"fillColor":"#ff6d00","fillOpacity":0.75}
))
flood_tainan_6h_150mm.add_child(folium.GeoJson(
    "flood_tainan_6h_150mm/geojson_format_flood4_6150.json",
    name="flood_tainan_6h_150mm",
    style_function=lambda x : {"stroke":False,"fillColor":"#dd2c00","fillOpacity":0.75}
))
flood_tainan_6h_150mm

folium.LayerControl().add_to(main_map)
main_map.save("map_for_environment.html")


