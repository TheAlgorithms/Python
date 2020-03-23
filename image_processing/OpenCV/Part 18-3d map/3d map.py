from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111,projection ='3d')

x = [1,2,6,7,7,6]
y = [3,6,4,7,4,7]
z = [3,6,7,4,7,4]

x1 = [-1,2,-6,-7,7,6]
y1 = [-3,-6,4,7,-4,7]
z1 = [3,-6,7,-4,7,-4]

ax.scatter(x,y,z)
ax.scatter(x1,y1,z1)
#Axes3D.plot_wireframe(x,y,z)   #Don't use that bcoz it is of previous version instead of use -> ax.plot(x,y,z)
##ax.plot(x,y,z)
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')


plt.show()
