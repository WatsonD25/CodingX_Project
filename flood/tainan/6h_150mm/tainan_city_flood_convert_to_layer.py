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


start_time=time.time() #new

image=cv2.imread("6h_150mm.png")
print(image.shape)

dim_1_pixel_y=2166
dim_2_pixel_x=2745
x_init=153848.8
y_init=2555987.5
pixel_length=10
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

for i in range(dim_1_pixel_y):
  flood_1=[]
  flood_2=[]
  flood_3=[]
  flood_4=[]
  for j in range(dim_2_pixel_x):
    print(i,j) #new
    if image[i,j,0]==232 and image[i,j,1]==208 and image[i,j,2]==169:
      pixel_data_flood1=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_flood1.append(output_coordinate)
      flood_1.append(pixel_data_flood1)
    elif image[i,j,0]==204 and image[i,j,1]==172 and image[i,j,2]==98:
      pixel_data_flood2=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_flood2.append(output_coordinate)
      flood_2.append(pixel_data_flood2)
    elif image[i,j,0]==178 and image[i,j,1]==122 and image[i,j,2]==56:
      pixel_data_flood3=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_flood3.append(output_coordinate)
      flood_3.append(pixel_data_flood3)
    elif image[i,j,0]==125 and image[i,j,1]==72 and image[i,j,2]==39:
      pixel_data_flood4=[]
      for k in range(4):
        input_coordinate=coordinate[i,j,k,:]
        output_coordinate=TM2toWGS(input_coordinate)
        #print(output_coordinate)
        pixel_data_flood4.append(output_coordinate)
      flood_4.append(pixel_data_flood4)
  for item in flood_1:
      item=item.append(item[0])
  for item in flood_2:
      item=item.append(item[0])
  for item in flood_3:
      item=item.append(item[0])
  for item in flood_4:
      item=item.append(item[0])
  with open("geojson_format_flood1_6150.json","r",encoding="utf-8") as geo1:
    geojson1 = json.load(geo1)
    for item in flood_1:
      geojson1["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson1=json.dumps(geojson1,indent=4)
    with open("geojson_format_flood1_6150.json","w",encoding="utf-8") as geo1_1:
      geo1_1.write(geojson1)
  with open("geojson_format_flood2_6150.json","r",encoding="utf-8") as geo2:
    geojson2 = json.load(geo2)
    for item in flood_2:
      geojson2["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson2=json.dumps(geojson2,indent=4)
    with open("geojson_format_flood2_6150.json","w",encoding="utf-8") as geo2_1:
      geo2_1.write(geojson2)
  with open("geojson_format_flood3_6150.json","r",encoding="utf-8") as geo3:
    geojson3 = json.load(geo3)
    for item in flood_3:
      geojson3["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson3=json.dumps(geojson3,indent=4)
    with open("geojson_format_flood3_6150.json","w",encoding="utf-8") as geo3_1:
      geo3_1.write(geojson3)
  with open("geojson_format_flood4_6150.json","r",encoding="utf-8") as geo4:
    geojson4 = json.load(geo4)
    for item in flood_4:
      geojson4["features"][0]["geometry"]["coordinates"][0].append(item)
    geojson4=json.dumps(geojson4,indent=4)
    with open("geojson_format_flood4_6150.json","w",encoding="utf-8") as geo4_1:
      geo4_1.write(geojson4)



end_time=time.time() #new
print("It takes", end_time-start_time, "seconds to run the code.") #new