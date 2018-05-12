import numpy as np
import matplotlib
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt

line = np.linspace(-3, 3, 100)


plt.plot(line, np.tanh(line), label="tanh")
plt.plot(line, np.maximum(line, 0), label="relu")
plt.legend(loc = "best")
plt.title("activation_fuction")


print(np.maximum(line, 0))
#plt.show()
