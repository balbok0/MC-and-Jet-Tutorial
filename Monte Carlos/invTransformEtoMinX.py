import numpy as np
from scipy import integrate
from scipy import special
from random import random
import matplotlib.pyplot as plt
import plotly.plotly as py

x = []
for i in range(10000):
    x.append(-1 + ( -1*np.exp(-5) + 1)*random())
y = []
for i in x:
    y.append(-np.log(-i))
print(y)

print(y)
plt.hist(y)
plt.title("e^-x Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()
url = py.plot_mpl(fig, filename='mpl-basic-histogram')