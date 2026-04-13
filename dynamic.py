import matplotlib.pyplot as plt
import numpy as np
import time

# Turn on interactive mode
plt.ion()

x = []
y = []

fig, ax = plt.subplots()

for i in range(1, 20):
    x.append(i)
    y.append(np.random.randint(1, 10))  # random values

    ax.clear()  # clear previous frame
    
    # Stair plot
    ax.step(x, y, where='mid')
    
    ax.set_title("Dynamic Stair Plot")
    ax.set_xlabel("Time")
    ax.set_ylabel("Value")

    plt.pause(0.5)  # delay for animation

plt.ioff()
plt.show()
