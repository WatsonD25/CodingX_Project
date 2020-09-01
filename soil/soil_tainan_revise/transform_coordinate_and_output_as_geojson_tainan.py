import numpy as np
from cv2 import cv2
from pyproj import Transformer
import json
import time #new

def TM2toWGS(lonlatlist):
  transformer = Transformer.from_crs("epsg:3826", "epsg:4326")
  lon_tm2=lonlatlist[0]
  lat_tm2=lonlatlist[1]
  lat_wgs,lon_wgs=transformer.transform(lon_tm2,lat_tm2)
  return [lon_wgs,lat_wgs]
# def geojson_format(layer):
#   geojson={
#             "type": "FeatureCollection",
#             "features": [
#               {
#                 "type": "Feature",
#                 "properties": {},
#                 "geometry": {
#                   "type": "MultiPolygon",
#                   "coordinates": [[layer]

#                   ]
#                 }
#               }
#             ]
#           }
#   return geojson

start_time=time.time() #new
image=cv2.imread("soil_tainan.png")
dim_1_pixel_y=image.shape[0]
dim_2_pixel_x=image.shape[1]
x_init=153800 #圖片原點pixel的左上角
y_init=2554700 #圖片原點pixel的左上角
pixel_length=100
coordinate=np.zeros([dim_1_pixel_y,dim_2_pixel_x,4,2])
for i in range(dim_1_pixel_y):
  for j in range(dim_2_pixel_x):
      coordinate[i,j,0,1]=y_init-pixel_length*i
      coordinate[i,j,0,0]=x_init+pixel_length*j
      coordinate[i,j,1,1]=y_init-pixel_length*i
      coordinate[i,j,1,0]=x_init+pixel_length*(j+1)
      coordinate[i,j,2,1]=y_init-pixel_length*(i+1)
      coordinate[i,j,2,0]=x_init+pixel_length*(j+1)
      coordinate[i,j,3,1]=y_init-pixel_length*(i+1)
      coordinate[i,j,3,0]=x_init+pixel_length*(j)
# print(coordinate)


for i in range(dim_1_pixel_y):
  soil_green=[]
  soil_yellow=[]
  soil_red=[]
  for j in range(dim_2_pixel_x):
    print(i,j) #new
    if image[i,j,0]==80 and image[i,j,1]==208 and image[i,j,2]==146:
      pixel_data_green=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_green.append(output_coordinate)
      soil_green.append(pixel_data_green)
    elif image[i,j,0]==0 and image[i,j,1]==255 and image[i,j,2]==255:
      pixel_data_yellow=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_yellow.append(output_coordinate)
      soil_yellow.append(pixel_data_yellow)
    elif image[i,j,0]==0 and image[i,j,1]==0 and image[i,j,2]==255:
      pixel_data_red=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_red.append(output_coordinate)
      soil_red.append(pixel_data_red)
  for item in soil_green:
      item=item.append(item[0])
  for item in soil_yellow:
      item=item.append(item[0])
  for item in soil_red:
      item=item.append(item[0])
  with open("geojson_format_green_tainan.json","r",encoding="utf-8") as geo1:
    geojson1 = json.load(geo1)
    for item in soil_green:
      geojson1["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson1=json.dumps(geojson1,indent=4)
    with open("geojson_format_green_tainan.json","w",encoding="utf-8") as geo1_1:
      geo1_1.write(geojson1)
  with open("geojson_format_yellow_tainan.json","r",encoding="utf-8") as geo2:
    geojson2 = json.load(geo2)
    for item in soil_yellow:
      geojson2["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson2=json.dumps(geojson2,indent=4)
    with open("geojson_format_yellow_tainan.json","w",encoding="utf-8") as geo2_1:
      geo2_1.write(geojson2)
  with open("geojson_format_red_tainan.json","r",encoding="utf-8") as geo3:
    geojson3 = json.load(geo3)
    for item in soil_red:
      geojson3["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson3=json.dumps(geojson3,indent=4)
    with open("geojson_format_red_tainan.json","w",encoding="utf-8") as geo3_1:
      geo3_1.write(geojson3)


end_time=time.time() #new
print("It takes", end_time-start_time, "seconds to run the code.") #new