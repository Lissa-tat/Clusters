
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sys
max_int = sys.maxsize
from matplotlib.widgets import Slider, Button


# coordinates, y_true = make_blobs( # BLOB - Binary Large OBject - большой бинарный файлы
#     n_samples = 180, 
#     centers = 6, 
#     cluster_std = 0.70, 
#     # random_state = 40
# )

def elbow(delta, coordinates): 

  
    total = []
    k = 1
    while True:
        idx = np.random.choice(len(coordinates), k, replace=False)
        centers = coordinates[idx]         
        centers, labels, total_sum = K_means(coordinates, k, centers, total_sum=0)
        total.append(total_sum)
   
        max_sum = np.max(total)
        # print(total_sum / max_sum)
        if total_sum / max_sum < delta:
           
            return total, k, centers, labels
    
        k += 1
   

def calculate_distance(coordinates, centers):
    distances = np.zeros((len(coordinates), len(centers)))
    
    for k, center in enumerate(centers):
        distances[:, k] = np.sqrt( np.sum( (coordinates-center) ** 2, axis=1) )
    return distances

def K_means(coordinates, k, centers, total_sum):
    tol = 1e-16
    old_centers = centers.copy()
    distances = calculate_distance(coordinates, centers)
    labels = np.argmin(distances, axis=1) # пошли по строчкам, в каждой строчке выбрали минимум. (Какой то текст)
   
    for j in range(k):
        if np.sum(labels == j) > 0: # проверяем, что кластер не пустой
            centers[j] = np.mean(coordinates[labels == j], axis = 0) 
            
   
    if np.max((centers - old_centers) ** 2) > tol:
        centers, labels, total_sum = K_means(coordinates, k, centers, total_sum)
        
    else:   
        for j in range(k):
            total_sum += np.sum(np.min((distances[labels == j])**2, axis=1)) # Квадратичное отклонение   
    return centers, labels, total_sum
    

def main(delta, coordinates):
   
    
    total, k, centers, labels = elbow(delta, coordinates)
    # print(k)
    return total, k, centers, labels


