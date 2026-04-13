import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sys
max_int = sys.maxsize
from matplotlib.widgets import Slider, Button


coordinates, y_true = make_blobs( # BLOB - Binary Large OBject - большой бинарный файлы
    n_samples = 150, 
    centers = 6, 
    cluster_std = 0.70, 
    # random_state = 40
)

np.save('data\Coords.npy', coordinates)

coordinates = np.load('data\Coords.npy')
print(len(coordinates[:, 0]))




