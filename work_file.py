import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 25, 0.1)
fig, axis = plt.subplots(1, 2, figsize=(15, 5))
plt.ylabel('sin(x)')
plt.xlabel('x')
axis[0].plot(np.sin(x))
axis[1].plot(np.cos(x))
plt.show()