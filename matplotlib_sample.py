import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()

x = np.random.randn(30)
y = np.sin(x) + np.random.randn(30)
plt.plot(x, y, "ro")
plt.show()
