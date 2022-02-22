import numpy as np
from numpy.core.fromnumeric import reshape
"""
#python list
py_list=[2,3,5,7,11,13]

#numpy array
np_array=np.array([2,3,5,7,11,13,17,19,23])


py_multi=[[1,2,3],[4,5,6]]
np_multi=np_array.reshape(3,3)#reshape boyutunu değiştirir

print(np_multi)
"""

#result=np.array([1,3,5,7,9])
#result=np.arange(1,10)#1ile 10 arasında sayılar dizisi
#result=np.arange(10,100,3)
#result=np.zeros(10)
#result=np.ones(10)
#result=np.linspace(0,1,4)
#result=np.random.randint(0,10)
#result=np.random.randint(0,2,8)
"""
np_array=np.arange(64)
np_multi=np_array.reshape(8,8)

print(np_multi.sum(axis=1))#satırların toplamını verir
print(np_multi.sum(axis=0))#sütunların toplamını verir
"""
"""
rnd_numbers=np.random.randint(1,100,10)
#print(rnd_numbers)
#result=rnd_numbers.max()
result=rnd_numbers.max()
result=rnd_numbers.min()
result=rnd_numbers.mean()
result=rnd_numbers.argmin()
result=rnd_numbers.argmax()

print(result)
"""
"""
numbers=np.array([[0,5,10],[15,20,25],[30,35,40]])
result=numbers[5]
result=numbers[3:5]
result=numbers[::-1]
result=numbers[:,2]
result=numbers[:,0]
result=numbers[:,0:2]

print(result)
"""
"""
arr1=np.arange(1,10)
arr2=arr1#referans


arrcopy=arr1.copy()

arr2[0]=5
arrcopy[0]=10000
print(arr1)
print(arrcopy)
print(arr2)
"""


