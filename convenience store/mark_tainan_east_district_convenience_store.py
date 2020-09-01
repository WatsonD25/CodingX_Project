# import csv 教學
# https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

#folium feature group reference
# https://stackoverflow.com/questions/42330802/can-i-add-a-sequence-of-markers-on-a-folium-map
# https://stackoverflow.com/questions/61263787/folium-featuregroup-in-python

# html換行教學
# https://progressbar.tw/posts/199

import csv
import folium


convenience_store=[]
with open('tainan_east_district_convenience_store.csv', newline='') as csvfile:
    rows=csv.reader(csvfile)
    for row in rows:
        convenience_store.append(row)
# print(convenience_store)

main_map = folium.Map(location=[23.000909, 120.223148],zoom_start=15)
tooltip='點擊獲取更多資訊'
popup=folium.Popup(html='<b>台南市東區大學路1號</b>',max_width=200)
folium.Marker(location=[22.996319990137735,120.21953003491251],tooktip=tooltip,popup=popup,icon=folium.Icon(color='red')).add_to(main_map)

convenience_store_marker=folium.FeatureGroup('7-11')

for store in convenience_store:
    tooltip = '點擊獲取更多資訊'
    popup=folium.Popup(html='<b>%s<br><br>%s</b>'%("店名："+store[0], "地址："+store[3]),max_width=100)
    folium.Marker(location=[eval(store[2]),eval(store[1])],popup=popup,tooltip=tooltip).add_to(convenience_store_marker)
    
convenience_store_marker.add_to(main_map)
folium.LayerControl().add_to(main_map)
main_map.save("mark_tainan_east_district_convenience_store.html")




