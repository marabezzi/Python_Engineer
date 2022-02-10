import numpy as np
import matplotlib.pyplot as plt

v = [2,4,6]
w = [4,2,6]

array = np.array([[0, 0, v[0], v[1], v[2]], 
                 [0, 0, w[0], w[1]], w[2]])

X, Y, V, W = zip(*array)
plt.figure()
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
ax = plt.gca()
ax.annotate(f'v({v[0]},{v[1]},{v[2]})', (v[0],v[1],v[2]),fontsize=14)
plt.scatter(v[0],v[1],v[3], s=10,c='red')
ax.annotate(f'w({w[0]},{w[1]},{w[2]})', (w[0],w[1]),fontsize=14)
plt.scatter(w[0], w[1], w[2], s=10,c='blue')
ax.quiver(X, Y, V, W, angles='xy', scale_units='xy',color=['r','b'],scale=1)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

plt.grid()
plt.draw()
plt.show()