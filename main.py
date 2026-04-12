
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
            centers[j] = np.mean(coordinates[labels == j], axis = 0) # это я поняла
            
   
    if np.max((centers - old_centers) ** 2) > tol:
        centers, labels, total_sum = K_means(coordinates, k, centers, total_sum)
        
    else:   
        for j in range(k):
            total_sum += np.sum(np.min((distances[labels == j])**2, axis=1)) # Квадратичное отклонение   
    return centers, labels, total_sum
    
# def main():
#     delta = 0.05
        
#     total, k, centers, labels = elbow(delta)
#     print(k)

#     plt.figure(figsize=(10, 8))
#     plt.scatter(coordinates[:, 0], coordinates[:, 1], c=labels, cmap='viridis', alpha=0.7, s=40)
#     plt.scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200)
#     plt.show()

#     plt.figure(figsize=(10, 8))
#     plt.plot(total)
#     plt.show()


# main()
#---------------------------------------------------
def main(delta, coordinates):
    # coordinates  = coordinates1
    
    total, k, centers, labels = elbow(delta, coordinates)
    # print(k)
    return total, k, centers, labels


# init_delta = 0.05


# total, k, centers, labels = main(coordinates[:,0], init_delta)
# x = np.linspace(0, k-1, k)
# # fig, ax = plt.subplots(2)
# fig, ax = plt.subplots(1, 2)

# line, = ax[0].plot(x, total, lw=2)
# # plt.set_xlabel('Time [s]')

# plt1 = ax[1].scatter(coordinates[:, 0], coordinates[:, 1], c=labels, cmap='viridis', alpha=0.7, s=40)
# plt2 = ax[1].scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200)
# ax[1].set_title(f"количество кластеров k = {k}")


# # Регулировка области графика для размещения ползунков
# fig.subplots_adjust(left=0.25, bottom=0.25)


# # Вертикальный ползунок для амплитуды
# axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
# amp_slider = Slider(ax=axamp, label="Delta", valmin=0, valmax=0.5, valinit=init_delta, orientation="vertical")

# # Функция для обновления графика при изменении значения ползунка
# def update(val):
#     total, k, centers, labels = main(x, amp_slider.val)
#     line.set_ydata(total)
#     line.set_data(range(k), total)
#     ax[0].set_xlim(0, k-1)
#     ax[0].set_ylim(0, max(total))
#     ax[0].set_title("поиск оптимального количесва кластеров")
    

#     ax[1].clear()
#     plt1 = ax[1].scatter(coordinates[:, 0], coordinates[:, 1], c=labels, cmap='viridis', alpha=0.7, s=40)
#     plt2 = ax[1].scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200)
#     ax[1].set_title(f"количество кластеров k = {k}")
    
#     fig.canvas.draw_idle()



# amp_slider.on_changed(update)

# # Кнопка для сброса ползунков к начальным значениям
# resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
# button = Button(resetax, 'Reset', hovercolor='0.975')

# def reset(event):
#     amp_slider.reset()

# button.on_clicked(reset)

# plt.show()


