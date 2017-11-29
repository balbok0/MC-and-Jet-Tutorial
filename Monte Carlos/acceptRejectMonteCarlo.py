import random
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
py.sign_in('balbok', 'wELiVSFkUAEkSAgvAgwO')
#pdf is gaussian, with max = 1 (exp(0) = 1)
# that's normal distribution
# norm should be > mean
sigma = 2
mean = 5
norm = 10
f = lambda x: norm*np.exp(-(x-mean)**2/(2*(sigma**2)))
xs = []
ys = []
final = []
i = -1
while len(final) < 10000:
    i += 1
    ys.append(random.random()*norm)
    xs.append(random.random()*norm)
    if(f(xs[i]) > ys[i]):
        final.append(xs[i])


plt.hist(final)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

fig = plt.gcf()
plot_url = py.plot_mpl(fig, filename='mpl-basic-histogram')