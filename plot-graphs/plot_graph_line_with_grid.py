import matplotlib.pyplot as plt
import numpy as np

x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [100, 130, 160, 190, 220, 250, 280, 310]

plt.title("Title Here")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y)

plt.grid()
plt.show()