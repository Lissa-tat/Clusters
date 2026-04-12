

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sys
max_int = sys.maxsize
# print(max_int)


# n = 150
# # k = 5

coordinates, y_true = make_blobs( # BLOB - Binary Large OBject - большой бинарный файлы
    n_samples = 20, 
    centers = 3, 
    cluster_std = 0.70, 
    random_state = 40
)

# np.save('coordinates.npy', coordinates)
# np.save('y_true.npy', y_true)


# Вспомогательные функции
# ------------------------------
# def generate_clusters - генерирует точки make_blobs-ом

# def save_points - сохраняет точки в формате .npy

# def load_points - сохраняет точки в формате .npy
# ------------------------------

# def elbow():
    
#     total = []
#     for k in range(1, 15):
#         total_sum = 0
#         # print("k", k)
#         idx = np.random.choice(len(coordinates), k, replace=False)
#         centers = coordinates[idx] 
#         centers, labels, total_sum = K_means(coordinates, k, centers, total_sum)
#         total.append(total_sum)
    
#     return total

# def find_opt_elbow(total):
#         # print(total)
#         for i in range(len(total) - 1):
#             if total[i] / total[i+1] < 1:
#                 # print(i, " __ ", total[i+1], "__", total[i], "___", total[i]/total[i+1])
              
#                 return (i+1) 
# -------------------------------------------------------


# def elbow2(delta):
    
#     total_sum = None

#     while True:
        # if(total_sum == None):
        #     total_sum = K_means()
        #     continue

#         new_total_sum = K_means()
        
#         if(np.abs(total_sum - new_total_sum) < delta):
#             return clusters
#         ...


# def elbow1():
    
#     total = []
#     total_sum_old = 10000000
#     for k in range(1, max_int):
#         total_sum = 0
#         # print("k", k)
#         totall = []
#         idx = np.random.choice(len(coordinates), k, replace=False)
#         centers = coordinates[idx] 
#         centers, labels, total_sum_new = K_means(coordinates, k, centers, total_sum)
#         totall.append(total_sum_new)
#         # total.append(total_sum)
#         # print("total_sum_old", total_sum_old)
#         # print("total_sum_new", total_sum_new) 
#         if total_sum_old / total_sum_new < 1 or k == 30:  
#             # print("total_sum", total_sum)
#             # print("total_sum_new", total_sum_new) 
#             return k + 1
#         else: 
#             total_sum_old = total_sum_new.copy()
#             # print("после элсе total_sum_new", total_sum_new) 
#             # print("после элсе total_sum_old", total_sum_old) 
#         print(totall)
#     # return total

# def find_opt_elbow(total):
#         # print(total)
#         for i in range(len(total) - 1):
#             if total[i] / total[i+1] < 1:
#                 # print(i, " __ ", total[i+1], "__", total[i], "___", total[i]/total[i+1])
              
#                 return (i+1) 


def calculate_distance(coordinates, centers):
    distances = np.zeros((len(coordinates), len(centers)))
    for k, center in enumerate(centers):
        distances[:, k] = np.sqrt( np.sum( (coordinates-center) ** 2, axis=1) )

    return distances


def K_means(coordinates, k, centers, total_sum):
   
    tol = 0.01
    old_centers = centers.copy()
    distances = calculate_distance(coordinates, centers)
    labels = np.argmin(distances, axis=1) 
   
    for j in range(k):
        if np.sum(labels == j) > 0: # проверяем, что кластер не пустой
            centers[j] = np.mean(coordinates[labels == j], axis = 0) # это я поняла
       
   
    # print("отклонение", np.sum((centers - old_centers) ** 2)) # прыгает?!!
   
    if np.sum((centers - old_centers) ** 2) > tol:
        centers, labels, total_sum = K_means(coordinates, k, centers, total_sum)
    
    else:   
        for j in range(k):
            total_sum += np.sum(np.min((distances[labels == j])**2, axis=1)) # Квадратичное отклонение
            # mean_total_sum += cluster[j]

        # print ("total_sum", total_sum)
    return centers, labels, total_sum
    


# coordinates = np.load('coordinates.npy')
# y_true = np.load('y_true.npy')

def main():
    k = 4
    idx = np.random.choice(len(coordinates), k, replace=False)
    centers = coordinates[idx] 
    total_sum = 0
    centers, labels, total_sum = K_means(coordinates, k, centers, total_sum)
    # centers, labels, total_sum = K_means()
   
    print(len(labels))
    print(labels)

    for j in range(k):
        print(len(coordinates[labels == j]))
    
    # Выделить метод локтя в отдельную функцию
    # Сделать нормальный критерий остановки для локтя
    # Передавать критерий остановки как параметр


    # k_opt = find_opt_elbow(total)
    # print("k_opt", k_opt)

    # plt.figure(figsize=(10, 8))
    # plt.scatter(coordinates[:, 0], coordinates[:, 1], c=labels, cmap='viridis', alpha=0.7, s=40)
    # plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=100)
    
    # for j in range(k):
    #     plt.text(centers[j, 0], centers[j, 1], f"{len(coordinates[labels == j])}", c = 'red', fontsize=16)
 

    plt.show()

    # print(total[-1])

    # plt.figure(figsize=(10, 8))
    # plt.plot(total)
    # plt.show()

    # fracs = [total[i+1]/total[i] for i in range(0, len(total) - 1)]

    # plt.figure(figsize=(10, 8))
    # plt.plot(fracs)
    # plt.show()

    # abses = [np.abs(total[i+1]-total[i]) for i in range(0, len(total) - 1)]

    # plt.figure(figsize=(10, 8))
    # plt.plot(abses)
    # plt.show()

main()