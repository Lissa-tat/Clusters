import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs




coordinates, y_true = make_blobs( # BLOB - Binary Large OBject - большой бинарный файлы
    n_samples = 180, 
    centers = 4, 
    cluster_std = 0.70, 
    # random_state = 40
)

# x = np.linspace(0, k-1, k)
# fig, ax = plt.subplots(2)
# fig, ax = plt.subplots()


plt.scatter(coordinates[:, 0], coordinates[:, 1], c = y_true, cmap='viridis', alpha=0.7, s=40)
plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200)

plt.show()
