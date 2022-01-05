import numpy as np
import matplotlib.pyplot as plt 

x = np.array([0.02, 0.07, 0.17, 0.19, 0.21])
y = np.array([0.031, 0.109, 0.265, 0.298, 0.329])

plt.xlabel('X numbers')
plt.ylabel('Y numbers')
plt.plot(x, y)
plt.show()