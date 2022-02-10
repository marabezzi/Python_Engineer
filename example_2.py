import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

a = [-2, 4, 3]
b = [1, 4, 0]

soa = np.array([[0, 0, 0, a[0], a[1], a[2]], [0, 0, 0, b[0], b[1], b[2]],
                [0, 0, 0, 2, 1, 0], [0, 0, 0, 0.5, 0.7, 0]])

X, Y, Z, U, V, W = zip(*soa)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([-1, 0.5])
ax.set_ylim([-1, 1.5])
ax.set_zlim([-1, 8])
plt.show()