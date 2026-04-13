
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import sys
max_int = sys.maxsize
from matplotlib.widgets import Slider, Button
from main import main


import matplotlib.image as image
from PIL import Image

import json


class App:
    def __init__(self):
        # self.coordinates = coordinates
        

        self.fig, self.ax = plt.subplots(1, 2)
        self.line, = self.ax[0].plot([0], [0], lw=2)
        
        self.fig.subplots_adjust(left=0.25, bottom=0.25)

        init_delta = 0.05
        # Вертикальный ползунок для амплитуды
        self.axamp = self.fig.add_axes([0.1, 0.25, 0.0225, 0.63])
        self.amp_slider = Slider(ax=self.axamp, label="Delta", valmin=0, valmax=0.5, valinit=init_delta, orientation="vertical")

        # amp_slider.on_changed(update)
        self.amp_slider.on_changed(self.update)

        # Кнопка для сброса ползунков к начальным значениям
        self.resetax = self.fig.add_axes([0.8, 0.025, 0.1, 0.04])
        self.button = Button(self.resetax, 'Reset', hovercolor='0.975')

        self.button.on_clicked(self.reset)
    

    def load_image(self, src: str):
        # Загрузка изображения
        img = Image.open(src)
        self.img = np.asarray(img)
      

    def load_points(self, src : str):
        with open(src, 'r') as f:
            self.points = np.array(json.load(f))
        
    def draw(self, total, k, centers, labels):

        self.line.set_data(range(k), total)
        self.ax[0].set_xlim(0, k-1)
        self.ax[0].set_ylim(0, max(total))
        self.ax[0].set_title("поиск оптимального количесва кластеров")
        
        self.ax[1].clear()
      
        self.ax[1].imshow(self.img)

        self.ax[1].scatter(self.points[:, 0], self.points[:, 1], c=labels, cmap='viridis', alpha=0.7, s=40)
        # self.ax[1].scatter(centers[:, 0], centers[:, 1], c='black', marker='x', s=200)
        for j in range(k):
            self.ax[1].text(centers[j, 0], centers[j, 1], f"{len(self.points[labels == j])}", c = 'red', fontsize=12)
       
        self.ax[1].set_title(f"количество кластеров k = {k}")


    def update(self, val):
        total, k, centers, labels = main(self.amp_slider.val, self.points)
        self.draw(total, k, centers, labels)

        self.fig.canvas.draw_idle()

    def reset(self, event):
        self.amp_slider.reset()
   
    def run(self, image_src: str, points_src: str):       
        self.load_image(image_src)
        self.load_points(points_src)

        total, k, centers, labels = main(self.amp_slider.val, self.points)
        self.draw(total, k, centers, labels)

        plt.show()


app = App()
app.run(image_src='data/image1.jpg', points_src='data/points.json')
# app.image()
