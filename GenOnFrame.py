import cv2
import numpy as np
import random
import imageio

GRID_CNT = 30

cv2.namedWindow('origin')
frame_height, frame_width = 600, 600
one_grid_height, one_grid_width = frame_height//GRID_CNT, frame_width//GRID_CNT
img = np.ones((frame_height, frame_width, 3), dtype=np.uint8) * 255.
for height in range(0, frame_height, one_grid_height):
    for width in range(0, frame_width, one_grid_width):
        cv2.rectangle(img, (height, width), (height+one_grid_height, width+one_grid_width), color=(0, 0, 0), thickness=2)
# cv2.imshow('origin',img)
# cv2.waitKey(0)

maze_frame = np.array([[0] * GRID_CNT] * GRID_CNT)

maze_gardener = [15, 15]

direction = np.array(['up', 'down', 'left', 'right'])
direction_dir = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right':[1, 0]}

maze_stack = []
maze_stack.append(maze_gardener)

processImage = []

process_cnt = 0
while(True):
    # 미로생성 완료 조건
    if len(maze_stack) == 0:
        break
    # 네 방향 다 막혀있다면 이전 위치로 이동한다.
    not_left, not_right, not_high, not_low = False, False, False, False
    # print(maze_gardener)
    if maze_gardener[0] == 0:
        not_left = True
    elif maze_frame[maze_gardener[0] - 1, maze_gardener[1]] > 0:
        not_left = True
    if maze_gardener[0] == GRID_CNT - 1:
        not_right = True
    elif maze_frame[maze_gardener[0] + 1, maze_gardener[1]] > 0:
        not_right = True
    if maze_gardener[1] == 0:
        not_low = True
    elif maze_frame[maze_gardener[0], maze_gardener[1] - 1] > 0:
        not_low = True
    if maze_gardener[1] == GRID_CNT - 1:
        not_high = True
    elif maze_frame[maze_gardener[0], maze_gardener[1] + 1] > 0:
        not_high = True
        
    if not_left and not_right and not_low and not_high:
        maze_gardener = maze_stack.pop(-1)
        continue
    direction_bool = np.array([not not_high, not not_low, not not_left, not not_right])
    can_go = np.array(direction[direction_bool])
    
    next_step = random.choice(can_go)
    
    moving_gardener = [int((maze_gardener[0] + 0.5 * direction_dir[next_step][0]) * one_grid_height), 
                       int((maze_gardener[1] + 0.5 * direction_dir[next_step][1]) * one_grid_width)]
    
    cv2.rectangle(img, (moving_gardener[0] + 3, moving_gardener[1] + 3),
                  (moving_gardener[0] + one_grid_height - 3, moving_gardener[1] + one_grid_width - 3),
                  color=(255, 255, 255),
                  thickness=-1)
    
    # processImage.append(img.astype('uint8').tolist())
    
    maze_gardener = [maze_gardener[0] + direction_dir[next_step][0], maze_gardener[1] + direction_dir[next_step][1]]
    maze_frame[maze_gardener[0], maze_gardener[1]] += 1
    maze_stack.append(maze_gardener)
    
    print(process_cnt)
    process_cnt += 1
    # print(maze_frame)

# imageio.mimsave('GENERATEMAZE.gif', processImage, 'GIF', duration=0.05)

cv2.imwrite('maze.jpg', img)
cv2.imshow('origin',img)
cv2.waitKey(0)
