# file = open('data\\Coords.txt', 'r')
# content = file.read()
# print(content)
# file.close()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Генерируем синтетический набор данных
X, y_true = make_blobs( # BLOB - Binary Large OBject - большой бинарный файлы
    n_samples=300, 
    centers=6, 
    cluster_std=0.60, 
    random_state=42
)

print("массив", X)
# print(y_true)

# Функция для расчета расстояний между точками и центроидами
def calculate_distances(X, centroids):
    distances = np.zeros((X.shape[0], len(centroids)))
    # print("///", X.shape[0])
    for k, centroid in enumerate(centroids):
        # print("k", k)
    # Евклидово расстояние между каждой точкой и центроидом
        distances[:, k] = np.sqrt( np.sum( (X-centroid) ** 2, axis=1) )
    #     print("centr", centroid)
    print(distances)
    return distances

 # Наша реализация алгоритма K-means
def kmeans(X, k, max_iters=10, tol=1e-2):
# Случайно выбираем начальные центроиды
    idx = np.random.choice(len(X), k, replace=False)
    centroids = X[idx]
    # print(len(X))
    # print(idx)

    for i in range(max_iters):
        # Сохраняем старые центроиды для проверки сходимости
        old_centroids = centroids.copy()

        # Рассчитываем расстояния и назначаем точки ближайшим центроидам
        distances = calculate_distances(X, centroids)
        labels = np.argmin(distances, axis=1)
        print("labels", labels)

    # Обновляем центроиды
    for j in range(k):
        if np.sum(labels == j) > 0: # проверяем, что кластер не пустой
            print("np.sum(labels == j)", np.sum(labels == j))
            centroids[j] = np.mean(X[labels == j], axis=0)

        # Проверяем сходимость
        if np.sum((centroids - old_centroids) ** 2) < tol:
            break

    return centroids,  labels

# # Запускаем алгоритм
k = 6
centroids, labels = kmeans(X, k)

# Визуализируем результаты
plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.7, s=40)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200)
plt.title('K-means кластеризация (k=4)')
plt.xlabel('Признак 1')
plt.ylabel('Признак 2')
plt.show()
