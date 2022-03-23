import cv2
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

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


def Original_Pattern(img,x,y):
    center = img[x][y]
    
    val_ab = []
    
    val_ab.append(get_pixel(img,center,x-1,y-1))
   
    val_ab.append(get_pixel(img,center,x-1,y))
    
    val_ab.append(get_pixel(img,center,x-1,y+1))
    
    val_ab.append(get_pixel(img,center,x,y+1))
    
    val_ab.append(get_pixel(img,center,x+1,y+1))
    
    val_ab.append(get_pixel(img,center,x+1,y))
    
    val_ab.append(get_pixel(img,center,x+1,y-1))
    
    val_ab.append(get_pixel(img,center,x,y-1))
    
    return val_ab


def Calculate_lbp(val_ab):
    power_val=np.array([1,2,4,8,16,32,64,128])
    
    val = 0
    
    for i in range(len(val_ab)):
        
        val += val_ab[i]*power_val[i]
        
    return val


def Is_Uniform(pattern):
    trans_count = 0
    for i in range(len(pattern)-1):
        if pattern[i] != pattern[i+1]:
            trans_count += 1
    return True if trans_count<=2 else False

def gridImg(img,height,width,x):
	grids=[]

	for k in range(height):
		for l in range(width):
				tempGrid=np.zeros((x,x))
				for i in range(x):
					for j in range(x):
						tempGrid[i][j]=img[k][l]
				grids.append(tempGrid)

	return grids				


img_bgr = cv2.imread("1tl.png")
original_pattern = []
lbp_values = []
height, width, _ = img_bgr.shape
uniform_count = 0

# We need to convert RGB image
# into gray one because gray
# image has one channel only.
img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

# Create a numpy array as
# the same height and width
# of RGB image
img_lbp = np.zeros((height, width),
				np.uint8)

for i in range(0, height):
	for j in range(0, width):
		original_pattern = Original_Pattern(img_gray,i,j)
		if Is_Uniform(original_pattern):
			calculatedLbp=Calculate_lbp(original_pattern)

			uniform_count += 1
            
			for k in range(8):
				rotated_pattern = np.roll(original_pattern,k)   
				lbp_values.append(Calculate_lbp(rotated_pattern))
            
			img_lbp[i][j] = min(lbp_values)
			lbp_values = []
		
		else:
			img_lbp[i][j]=10


plt.imshow(img_bgr)
plt.show()

plt.imshow(img_lbp, cmap ="gray")
plt.show()

print("LBP Program is finished")
print(uniform_count)