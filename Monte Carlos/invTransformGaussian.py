import numpy as np
from scipy import integrate
from scipy import special
from random import random
import matplotlib.pyplot as plt
import plotly.plotly as py

mean = 5
sigma = 2
domain = [0, 10]

max = integrate.quad(lambda x: np.exp(-np.square((x-mean)/sigma)/2)/np.sqrt(2*sigma*np.pi), -np.inf, 10)[0]
min = integrate.quad(lambda x: np.exp(-np.square((x-mean)/sigma)/2)/np.sqrt(2*sigma*np.pi), -np.inf, 0)[0]
x = []
for i in range(10000):
    x.append((max-min)*random() + min)
y = []
for i in x:
    y.append((mean + sigma*np.sqrt(2)*special.erfinv(2*i/np.sqrt(sigma) - 1)))
print(y)


plt.hist(y)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()
url = py.plot_mpl(fig, filename='mpl-basic-histogram')
