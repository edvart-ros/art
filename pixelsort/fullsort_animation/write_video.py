import cv2 as cv

img = cv.imread('sc_full_sort_0.png')
size = (img.shape[1], img.shape[0])

result = cv.VideoWriter('animation.mp4', 
                        cv.VideoWriter_fourcc(*'mp4v'), 
                        60, size)


for i in range(1001):
    path = f"sc_full_sort_{i}.png"
    img = cv.imread(path)
    result.write(img)

result.release()