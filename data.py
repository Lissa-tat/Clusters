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

# coordinates = np.load('data\Coords.npy')
# print(coordinates[0])


# with open('data\coordinates.txt', 'w') as testfile:
#     for row in coordinates:
#         # testfile.write(' '.join([str(a) for a in row]) + '\n')
#         testfile.write(row)

# import json

# with open('data/datafile.json', 'w', encoding='utf-8') as f:
#     json.dump(coordinates.tolist(), f)


# with open('data\coordinates.txt', 'r') as testfile:
#     for row in testfile:
#         coor = np.array(testfile.read())



# print(coor)



