import cv2
import numpy as np
from matplotlib import pyplot as plt
#PURPOSE:Önce düz paranın rlbp değerine bakacağız sonra döndürüp tekrar bakacağız.
	
def get_pixel(img, center, x, y):
	
	new_value = 0
	
	try:
		# If local neighbourhood pixel
		# value is greater than or equal
		# to center pixel values then
		# set it to 1
		if img[x][y] >= center:
			new_value = 1
			
	except:
		# Exception is required when
		# neighbourhood value of a center
		# pixel value is null i.e. values
		# present at boundaries.
		pass
	
	return new_value

# Function for calculating LBP
def lbp_calculated_pixel(img, x, y):

	center = img[x][y]
	val_ar = []
	try:
		# top_left
		val_ar.append(img[x-1, y-1])
		
		# top
		val_ar.append(img[x-1, y])
		
		# top_right
		val_ar.append(img[x-1, y + 1])
		
		# right
		val_ar.append(img[x, y + 1])
		
		# bottom_right
		val_ar.append(img[x + 1, y + 1])
		
		# bottom
		val_ar.append(img[x + 1, y])
		
		# bottom_left
		val_ar.append(img[x + 1, y-1])
		
		# left
		val_ar.append(img[x, y-1])
	except:
		pass
	###
    #compare every neighbours with center ,the index of the farest is the one we need
	farest=0
	global index
	index=0
	for i in range(len(val_ar)):
		if abs(center-val_ar[i])>=farest:
			farest=val_ar[i]
			index=i

	for i in range(len(val_ar)):
		if val_ar[i]>=center:
			val_ar[i]=1
		else:
			val_ar[i]=0

	# Now, we need to convert binary
	# values to decimal
	#####here we need to create power_val dynamic
	power_val = [1, 2, 4, 8, 16, 32, 64, 128]
	j=0
	for i in range(index,index+8):
		rightIndx=i%8
		power_val[rightIndx]=2**j
		j+=1


	val = 0
	
	for i in range(len(val_ar)):
		val += val_ar[i] * power_val[i]
		
	return val

path = 'joker.jpg'
img_bgr = cv2.imread(path, 1)

height, width, _ = img_bgr.shape

# We need to convert RGB image
# into gray one because gray
# image has one channel only.
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Create a numpy array as
# the same height and width
# of RGB image
img_lbp = np.zeros((height, width), np.uint8)

for i in range(0, height):
	for j in range(0, width):
		img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)


plt.imshow(img_bgr)

plt.show()

plt.imshow(img_lbp, cmap ="gray")
plt.show()

print("LBP Program is finished")


plt.hist(img_lbp.flat,bins=100,range=(0,255),rwidth=0.95)
plt.show()