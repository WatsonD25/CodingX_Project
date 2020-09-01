# import csv 教學
# https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/

#folium feature group reference
# https://stackoverflow.com/questions/42330802/can-i-add-a-sequence-of-markers-on-a-folium-map
# https://stackoverflow.com/questions/61263787/folium-featuregroup-in-python

# html換行教學
# https://progressbar.tw/posts/199


import folium


## 預期從DB中搜尋的方法：
# 輸入地址的TM2度座標為(x,y)，若要找半徑1 km之內的目標物(座標為(x',y'))，
# DB search的篩選條件為 x-1000<=x'<=x+1000，y-1000<=y'<=y+1000
# 並輸出符合的資料成一個雙層list,第一層的元素為個別目標物，第二層元素(2個)為TM2的座標
# 將雙層list在此進行距離運算，符合距離的即加入map中
# 如果在DB搜尋時就可以用運算篩選，評估符合效率後可直接運算距離來篩選

target_location=[] # 待傳入
radius= # 待傳入
convenience_store=[[]] # 待傳入

main_map = folium.Map(location=[23.000909, 120.223148],zoom_start=15)
convenience_store_marker=folium.FeatureGroup('7-11')

for store in convenience_store:
    if ((store[0]-target_location[0])**2+(store[1]-target_location[1])**2)**0.5<=radius
      tooltip = '點擊獲取更多資訊'
      popup=folium.Popup(html='<b>%s<br><br>%s</b>'%("店名："+store[0], "地址："+store[3]),max_width=100)
      folium.Marker(location=[store[2],store[1]],popup=popup,tooltip=tooltip).add_to(convenience_store_marker)

convenience_store_marker.add_to(main_map)
folium.LayerControl().add_to(main_map)
main_map.save("mark_tainan_east_district_convenience_store.html")




