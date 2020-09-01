import folium

main_map = folium.Map(location=[23.000909, 120.223148],zoom_start=12)




folium.LayerControl().add_to(main_map)
main_map.save("map_for_environment.html")


