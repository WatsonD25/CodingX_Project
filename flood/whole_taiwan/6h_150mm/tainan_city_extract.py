import numpy as np
from cv2 import cv2

image=cv2.imread("6h_150mm.png")
dim_1_pixel_y=1051
dim_2_pixel_x=1009
x_init=153840
y_init=2555320

tinan_city_extract=np.zeros([dim_1_pixel_y,dim_2_pixel_x,4,2])
for i in range(12828,13879):
    for j in range(192,2001):
        tinan_city_extract[i,j,0,1]=y_init-pixel_length*i
        tinan_city_extract[i,j,0,0]=x_init+pixel_length*j
        tinan_city_extract[i,j,1,1]=y_init-pixel_length*i
        tinan_city_extract[i,j,1,0]=x_init+pixel_length*(j+1)
        tinan_city_extract[i,j,2,1]=y_init-pixel_length*(i+1)
        tinan_city_extract[i,j,2,0]=x_init+pixel_length*(j+1)
        tinan_city_extract[i,j,3,1]=y_init-pixel_length*(i+1)
        tinan_city_extract[i,j,3,0]=x_init+pixel_length*(j)
    
print(image.shape)
print(image)