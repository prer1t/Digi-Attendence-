#importing the required libraries

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

#first trying the model on a simpler photo 
#then implementing on classroom's image

img=cv.imread('TS3.jpg',cv.IMREAD_GRAYSCALE)

#printing the image 

plt.imshow(img,cmap='gray',interpolation='bicubic')




