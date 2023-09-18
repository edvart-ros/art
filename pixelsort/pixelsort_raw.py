import numpy as np
import cv2 as cv
import time

img_name = 'sc_full_sort_0'

img = cv.cvtColor(cv.imread(img_name + '.png'), cv.COLOR_BGR2RGB)
rows, cols, channels = img.shape

sorted_img = np.zeros_like(img)
for i in range(cols):
    col_rgb = img[:, i, :]
    col_hue = col_rgb[:,0]*0.2126 + col_rgb[:,1]*0.7152+col_rgb[:,2]*0.0722
    hue_sort_inds = col_hue.argsort()
    col_rgb_sorted = col_rgb[hue_sort_inds]
    sorted_img[:,i] = col_rgb_sorted

cv.imwrite(f"{img_name}_dumb_sort.png", cv.cvtColor(sorted_img,cv.COLOR_BGR2RGB))
