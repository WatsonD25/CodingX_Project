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


folium.LayerControl().add_to(main_map)
main_map.save("map_for_environment.html")


