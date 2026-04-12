import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
np.random.seed(0)
x = np.random.uniform(0.0,10.0,15)
y = np.random.uniform(0.0,10.0,15)

datafile = 'data\im1.jpg'
img = plt.imread(datafile)
plt.scatter(x,y,zorder=1)
# plt.imshow(img, zorder=0.5, extent=[0.5, 8.0, 1.0, 7.0])
plt.plot([1,2,3],[5,3,7])

fig.figimage(img, 25, 25, alpha=0.5, zorder=3) 
plt.show()
