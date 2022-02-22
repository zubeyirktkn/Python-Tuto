import matplotlib.pyplot as plt
import numpy as np



x=[0,1,2,3,4,5,6,7,8,9]#kaçıncı hamle
yb=[20,22,24,30,20,24,23,26,24,32]#beyaz için  valid moves
ys=[20,21,25,20,17,19,13,16,15,23]#siyah için valid moves
#plt.plot(x,y,"--g")
#plt.plot(x,y,color="red",linewidth="5")
plt.plot(x,yb,"o-r",label="White")
plt.plot(x,ys,"o-b",label="Black")

plt.axis([0,20,0,60])#bu lazım kaçıncı hamle

plt.title("Başlık")
plt.xlabel("kaçıncı hamlede olduğu")
plt.ylabel("yapılabilecek hamle sayısı")

plt.legend()
plt.show()


"""
x=np.linspace(0,2,100)

plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")

plt.xlabel("xlabel")
plt.ylabel("ylabel")

plt.legend()#labelları gösteriyor plota özel olan labelları


plt.show()
"""

"""
x=np.linspace(0,2,100)

fig,axs=plt.subplots(2)
axs[0].plot(x,x,color="red")
axs[1].plot(x,x**2,color="blue")


plt.show()
"""


#figure oluşturma

#x=np.linspace(-10,9,20)
#y=x**3
#z=x**2



"""
fig=plt.figure()
axes_cube=fig.add_axes([0.2,0.2,0.6,0.6])

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Cube")

axes_square=fig.add_axes([0.3,0.6,0.2,0.2])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("X axis")
axes_square.set_ylabel("Y axis")
axes_square.set_title("Square")
"""
"""
fig=plt.figure()

axes=fig.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=4)
"""
"""
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4))
axes[0].plot(x,y)
axes[0].set_title("Square")
axes[1].plot(x,z)
axes[1].set_title("Cube")
plt.tight_layout()

fig.savefig("figure1.png")



plt.show()
"""