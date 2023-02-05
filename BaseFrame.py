import cv2
import numpy as np

cv2.namedWindow('origin')
frame_height, frame_width = 600, 600
grid_cnt = 20
one_grid_height, one_grid_width = frame_height//grid_cnt, frame_width//grid_cnt
img = np.ones((frame_height, frame_width, 3), dtype=np.uint8) * 255.
for height in range(0, frame_height, one_grid_height):
    for width in range(0, frame_width, one_grid_width):
        cv2.rectangle(img, (height, width), (height+one_grid_height, width+one_grid_width), color=(0, 0, 0), thickness=2)
cv2.imshow('origin',img)
cv2.waitKey(0)