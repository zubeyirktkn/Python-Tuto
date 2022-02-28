import cv2 as cv
import numpy as np
import random as rd

#read image
img=cv.imread("white300x300.png")

#resize image 500x500
img500x500=cv.resize(img,(500,500))

#saving 500x500 img
cv.imwrite("white500x500.png",img500x500)

#changing all pixels randomly
for x in range(20):
    for i in range(0,500):
        for j in range(0,500):
            randG=rd.randint(0,256)
            randB=rd.randint(0,256)
            randR=rd.randint(0,256)
            img500x500[i,j]=[randG,randB,randR]
    cv.imwrite("image"+str(x)+".png",img500x500)

#cv.imshow("",img500x500)
print(img500x500[250,250])
cv.waitKey(0)#waits for pressing a button
cv.destroyAllWindows()