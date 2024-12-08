import re
import os

input_name = "input_6.txt"
input_path = "inputs/" + input_name
# in macOS or pycharm, ".." is needed to get out of "code" directory,
# in Windows or VSCode, the starting point is the repository directory

file = open(os.path.abspath(input_path), "r")
input_data = file.read()
file.close()

input_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


input_data = input_data.splitlines()

for r,line in enumerate(input_data):
    col = re.search(r"([\^><v])", line)
    if col is not None:
        position = col.start(),r
        direction = col.string[col.start():col.end()]



def go_up(map_list, position):
    x,y = position
    count = 0
    while y-1 >= 0 and map_list[y-1][x] != "#":
        map_list[y] = map_list[y][:x] +  "X" + map_list[y][x+1:]
        count += 1
        y -= 1
        if y==0:
            return count, (x,y), None, map_list
    return count, (x,y), ">", map_list

def go_down(map_list, position):
    x, y = position
    count = 0
    while y+1 < len(map_list) and map_list[y+1][x] != "#":
        map_list[y] = map_list[y][:x] +  "X" + map_list[y][x+1:]
        count += 1
        y += 1
        if y == len(map_list)-1:
            return count, (x,y), None, map_list
    return count, (x,y), "<", map_list

def go_right(map_list, position):
    x, y = position
    count = 0
    while x+1 < len(map_list[0]) and map_list[y][x+1] != "#":
        map_list[y] = map_list[y][:x] +  "X" + map_list[y][x+1:]
        count += 1
        x += 1
        if x == len(map_list[0])-1:
            return count, (x,y), None, map_list
    return count, (x,y), "v", map_list

def go_left(map_list, position):
    x, y = position
    count = 0
    while x-1 >= 0 and map_list[y][x-1] != "#":
        map_list[y] = map_list[y][:x] +  "X" + map_list[y][x+1:]
        count += 1
        x -= 1
        if x == 0:
            return count, (x,y), None, map_list
    return count, (x,y), "^", map_list


def go_to_next_obstacle(map_list, position, direction):
    if direction == "^":
        return go_up(map_list, position)

    if direction == "v":
        return go_down(map_list, position)

    if direction == ">":
        return go_right(map_list, position)

    if direction == "<":
        return go_left(map_list, position)

cnt = 1
pos , dirn , new_map = position, direction, input_data
data = [(position, direction)]
while pos is not None:
    temp_cnt, pos, dirn, new_map = go_to_next_obstacle(new_map, pos, dirn)
    print(temp_cnt, pos, dirn)
    cnt += temp_cnt
    data.append((pos, dirn))
    if dirn is None:
        print("End of map")
        break

cnt_new = 0

for line in new_map:
    cnt_new += line.count("X")

print(cnt_new + 1)

obstacle = 0
for i in range(len(data)-1):
    if i <= 3:
        continue
    if data[i-1][1] == "<":
        if data[i][0][0] < data[i-3][0][0]:
            x,y = data[i-3][0][0]-1, data[i][0][1]
            new_map[y] = new_map[y][:x] +  "O" + new_map[y][x+1:]
            obstacle +=1
    elif data[i-1][1] == "^":
        if data[i][0][1] < data[i-3][0][1]:
            x,y = data[i][0][0], data[i-3][0][1]-1
            new_map[y] = new_map[y][:x] +  "O" + new_map[y][x+1:]
            obstacle +=1
    elif data[i-1][1] == ">":
        if data[i][0][0] > data[i-3][0][0]:
            x,y = data[i-3][0][0]+1, data[i][0][1]
            new_map[y] = new_map[y][:x] +  "O" + new_map[y][x+1:]
            obstacle +=1
    elif data[i-1][1] == "v":
        if data[i][0][1] > data[i-3][0][1]:
            x,y = data[i][0][0], data[i-3][0][1]+1
            new_map[y] = new_map[y][:x] +  "O" + new_map[y][x+1:]
            obstacle +=1
    elif data[i][1] == None:
        pass
    # todo: add extra obstacles on edges of the map
    # todo: add extra obsactles that can go back to previously found loops
    # todo: consider a dictionary based on the direction to find the right coordinates

print(obstacle)

for line in new_map:
    print(line)

