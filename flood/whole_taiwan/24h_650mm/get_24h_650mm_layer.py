# https://fr-fr.facebook.com/HSNUCTG/posts/1183076225064594/
# ●台灣本島最北端之富貴角(東經121.52度,北緯25.29度)
# TWD97 TM2台灣→(300351,2797992)
# ●台灣本島最東端之三貂角(東經122.00度,北緯25.00度)
# TWD97 TM2台灣→(351202,2767077)
# ●台灣本島最西端之外傘頂洲(東經120.03度,北緯23.50度)
# TWD97 TM2台灣→(150929,2599985)
# ●台灣本島最南端之鵝鑾鼻燈塔(東經120.80度,北緯21.87度)
# TWD97 TM2台灣→(234752,2422656)



# download image 參考以下網址程式碼
# https://towardsdatascience.com/how-to-download-an-image-using-python-38a75cfa21c

# datetime format 參考以下網址
# http://python-learnnotebook.blogspot.com/2018/10/python-datetime-format.html
# Import Necessary Modules

# 字串黏接 參考以下網址
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p14_combine_and_concatenate_strings.html
import requests # to get image form the web
import shutil # to save it locally
import numpy as np
from cv2 import cv2
import os 
import time



start_time=time.time()

print(os.getcwd())
# Set up the image URL and filename
image_url_1 = "https://dwgis.ncdr.nat.gov.tw/arcgis/services/PotentialFlood3/24H_650mm/MapServer/WMSServer?BBOX="
image_url_2 = "&WIDTH=915&HEIGHT=722&SIZE=915,722&REQUEST=GetMap&SERVICE=WMS&BGCOLOR=0xFFFFFF&TRANSPARENT=TRUE&SRS=EPSG:3826&LAYERS=0&VERSION=1.1.1&FORMAT=image/png&STYLES="

flag_y=0
for i in range(150000,352000,18300):
    x1=str(i)
    x2=str(i+18300)
    flag = 0
    for j in range (2422000,2800000,14440):
        y1=str(j)
        y2=str(j+14440)
        image_url = image_url_1+x1+","+y1+","+x2+","+y2+image_url_2
        # print(image_url)
        r = requests.get(image_url, stream=True)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            #Set decode_content calue to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a file in destination with wb (write binary) perminssion.
            with open("image_now.png", "wb") as f:
                shutil.copyfileobj(r.raw, f)
        else:
            print(r.status_code)
            print(image_url)
            print("Image couldn\'t be retrieved.") 
        if flag==0:
            image0=cv2.imread("image_now.png",cv2.IMREAD_UNCHANGED)
            cv2.imwrite("image_old.png",image0)
        else:
            image1=cv2.imread("image_now.png",cv2.IMREAD_UNCHANGED)
            image2=cv2.imread("image_old.png",cv2.IMREAD_UNCHANGED)
            image2=np.concatenate((image1,image2),axis=0)
            cv2.imwrite("image_old.png",image2)
        flag = flag +1
    if flag_y==0:
        image5=cv2.imread("image_old.png",cv2.IMREAD_UNCHANGED)
        cv2.imwrite("image_old_y.png",image5)
    else:
        image3=cv2.imread("image_old_y.png",cv2.IMREAD_UNCHANGED)
        image4=cv2.imread("image_old.png",cv2.IMREAD_UNCHANGED)
        image3=np.concatenate((image3,image4),axis=1)
        cv2.imwrite("image_old_y.png",image3)
    flag_y=flag_y+1

end_time=time.time()
print("It takes", end_time-start_time, "seconds to run the code.")
    


