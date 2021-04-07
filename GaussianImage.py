import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import csv



# https://stackoverflow.com/questions/3279560/reverse-colormap-in-matplotlib
from PIL import Image


def return_gaussian(pts):
    sigma = 5
    peaks_img = np.zeros((512, 512))
    peaks_img[np.int_(pts[:, 1]), np.int_(pts[:, 0]) ] = 1
    density_img = cv2.GaussianBlur(peaks_img, (0, 0), sigma)
    return density_img

path = 'annotations' + os.sep + 'gaussian_images'
landmark_path = 'annotations' + os.sep + 'landmarks'

if not os.path.exists(path):
    os.makedirs(path)

subfolders = [f.path for f in os.scandir(landmark_path) if f.is_dir()]
for folder in subfolders:
    for csv_file in os.scandir(folder):
        with open(csv_file.path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            rows = list(reader)
            location = np.array([[int(rows[1][0]),512 - int(rows[1][1])]])
            image = return_gaussian(location)
            dest_folder = folder.replace('landmarks', 'gaussian_images')
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            destinations = (dest_folder + os.sep + csv_file.name).replace('.csv', '.png')
            #print(destinations)
            plt.imsave(destinations, image, cmap='Greys_r')

            """
            image = Image.open(destinations)
            new_image = image.resize((388, 388))
            new_image.save(destinations.replace('.png','_r.png'))
            """






# image = return_gaussian(np.array([[50, 15]]) )
# plt.imshow(image, cmap='Greys_r')
# plt.show()
