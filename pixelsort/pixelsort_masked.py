import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img_name = 'sc'
img = cv.imread(img_name + '.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
rows, cols, channels = img.shape

n = 1000
for i in range(n+1):
    thresh = np.max(img_gray)*(i/n)
    mask = (img_gray <= thresh).astype(int)
    sorted_img = img.copy()

    for j in range(rows):
        row_rgb = img[j, :, :]
        row_gray = img_gray[j]
        mask_row = mask[j].astype(int)

        # Get start and end indices of spans using numpy
        diffs = np.diff(np.insert(mask_row, [0, mask_row.size], [0, 0]))
        starts = np.where(diffs == 1)[0]
        ends = np.where(diffs == -1)[0]

        for [start, end] in zip(starts, ends):
            span_rgb = row_rgb[start:end]
            span_metric = row_gray[start:end]

            sort_inds = span_metric.argsort()
            span_rgb_sorted = span_rgb[sort_inds]
            sorted_img[j][start:end] = span_rgb_sorted

    cv.imwrite(f"fullsort_animation/{img_name}_full_sort_{i}.png", sorted_img)
