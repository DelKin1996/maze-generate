import numpy as np
import random

GRID_CNT = 20

maze_frame = np.array([[0] * GRID_CNT] * GRID_CNT)

maze_gardener = [0, 0]

direction = np.array(['up', 'down', 'left', 'right'])
direction_dir = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right':[1, 0]}

maze_stack = []
maze_stack.append(maze_gardener)
while(True):
    # 미로생성 완료 조건
    if len(maze_stack) == 0:
        break
    # 네 방향 다 막혀있다면 이전 위치로 이동한다.
    not_left, not_right, not_high, not_low = False, False, False, False
    print(maze_gardener)
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
    # 틀을 벗어나지 못하게 한다.
    direction_bool = np.array([not not_high, not not_low, not not_left, not not_right])
    # 정원사의 다음 이동방향
    print(direction_bool)
    can_go = np.array(direction[direction_bool])
    
    next_step = random.choice(can_go)
    print(next_step)
    maze_gardener = [maze_gardener[0] + direction_dir[next_step][0], maze_gardener[1] + direction_dir[next_step][1]]
    maze_frame[maze_gardener[0], maze_gardener[1]] += 1
    maze_stack.append(maze_gardener)
    
print(maze_frame)