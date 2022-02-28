import cv2
from cv2 import imread
from cv2 import imshow
from matplotlib.image import imsave
import numpy as np

"""
#lesson1 read,show,print the attributes
img= cv2.imread("joker.jpg",0)#reads the image/second parametre (0) turns image gray

cv2.imshow("Zet",img)#shows the image
#cv2.imwrite("jokerGray.jpg",img)#saves gray image 

#print(img)#prints the matrix of the img
#print(img.size)#prints the size of the img
#print(img.dtype)#prints the type of the img
print(img.shape)#(hight,width,channelnum)

"""
#----------------------------------------------------------
"""
#lesson2 accessing pixels
img=cv2.imread("joker.jpg")
cv2.imshow("joker",img)

print(img[(0,0)])
print(img.shape)
"""
#----------------------------------------------------------
"""
#lesson3 changing pixels
img=cv2.imread("joker.jpg")
#img[250,400]=[255,255,255]#makes white the choosen pixel

for i in range(230,300):
    for j in range(240,470):
        img[i,j]=[0,0,0]
        

cv2.imshow("joker",img)
#cv2.imwrite("jokerCensored.jpg",img)
"""
#----------------------------------------------------------
"""
#lesson4 effecting
img=cv2.imread("joker.jpg")

#img[:,:,2]=154
#img[:,:,1]=27
img[230:300,240:470,0]=255#firs two parameter to choose the pixels,third one to choose the channel
img[230:300,240:470,1]=255

cv2.imshow("joker",img)
"""
#----------------------------------------------------------

"""
#cropping and merging images
img=cv2.imread("joker.jpg")
imgCropped=img[230:300,240:470]
imgCropped[:,:,0]=255
img[0:70,0:230]=imgCropped
img[300:370,470:700]=imgCropped
img[100:150,200:250]=(0,0,255)

#cv2.imshow("imgCropped",imgCropped)
cv2.imshow("jokerEye",img)
"""
#----------------------------------------------------------

"""
#reflecting replicating etc.
img=cv2.imread("joker.jpg")
imgMirrored=cv2.copyMakeBorder(img,400,0,0,0,cv2.BORDER_REFLECT)
imgReplicated=cv2.copyMakeBorder(img,400,0,0,0,cv2.BORDER_REPLICATE)
imgWrapped=cv2.copyMakeBorder(img,400,0,0,0,cv2.BORDER_WRAP)
imgConstanted=cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_CONSTANT,
                                value=(0,0,255))

cv2.imshow("Joker",imgMirrored)
cv2.imshow("Joker",imgReplicated)
cv2.imshow("Joker",imgWrapped)
cv2.imshow("Joker",imgConstanted)
"""
#----------------------------------------------------------

"""
#drawing rectangle
img=imread("joker.jpg")

cv2.rectangle(img,(200,300),(500,200),[0,0,255],3)

cv2.imshow("",img)
"""
#----------------------------------------------------------
"""
#pixel+pixel
img=imread("joker.jpg")
img2=imread("joker2.jpg")

pixel1=img[200,200]
pixel2=img2[200,200]

print(str(pixel1)+"+"+str(pixel2)+"="+str(pixel1+pixel2))
"""
#----------------------------------------------------------
"""
#merging imgs together

img=imread("joker.jpg")
img2=imread("joker2.jpg")

#sum=cv2.add(img2,img)#if size of the images are matched you can merge them together
sumWeighted=cv2.addWeighted(img2,0.3,img,0.7,0)

cv2.imshow("",sumWeighted)
"""
#----------------------------------------------------------
"""
#making image gray
img=imread("joker2.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("",imgGray)
"""
#----------------------------------------------------------
"""
#image scaling 2xUp n down
img=imread("joker.jpg")

img2xBigger=cv2.pyrUp(img)
img2xSmaller=cv2.pyrDown(img)

cv2.imshow("Original image",img)
#cv2.imshow("2x Bigger image",img2xBigger)
cv2.imshow("2x Smaller image",img2xSmaller)

print(img.shape)
print(img2xBigger.shape)
print(img2xSmaller.shape)
"""
#----------------------------------------------------------
"""
#resizing img freely
img=cv2.imread("joker.jpg")
imgRszd=cv2.resize(img,(300,300))
cv2.imwrite("joker300x300.jpg",imgRszd)

cv2.imshow("",img)
cv2.imshow("",imgRszd)
"""
#----------------------------------------------------------

img=np.zeros((300,300,3),dtype="uint8")
print(img)


cv2.waitKey(0)#waits for pressing a button
cv2.destroyAllWindows()