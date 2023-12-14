import time

with open('input_10.txt', encoding='utf-8') as txt:
    data = txt.readlines()

up = ['|', '7', 'F']
left = ['-', 'L', 'F']
right = ['-', 'J', '7']
down = ['|', 'J', 'L']
trans = {'S': [up, left, right, down], '|': [up, down], '7': [left, down], 'F': [right, down],
         '-': [left, right], 'L': [up, right], 'J': [up, left]}

closed_dict = {}
open_dict = {}

# Find S (the animal), add to open_dict as (y, x)
animal_break = False
for line in range(len(data)):
    if animal_break:
        break
    for idx, sym in zip(range(len(data[line])), data[line]):
        if sym == 'S':
            open_dict['S'] = (int(line), int(idx))
            animal_break = True
            break

# print(open_dict)
open_dict = [('S', open_dict['S'], 0)]
closed_dict = []
closed_distance_dict = []
# print(open_dict)
furthest = 0

while open_dict:
    y, x = open_dict[0][1]
    furthest = open_dict[0][2] + 1
    # check up
    if up in trans[open_dict[0][0]] and y > 0 and data[y-1][x] in up and open_dict[0][:2] not in closed_dict:
        open_dict.append((data[y-1][x], (y-1, x), furthest))
    # check left
    if left in trans[open_dict[0][0]] and x > 0 and data[y][x-1] in left and open_dict[0][:2] not in closed_dict:
        open_dict.append((data[y][x-1], (y, x-1), furthest))
    # check right
    if right in trans[open_dict[0][0]] and x < (len(data[0])-2) and data[y][x+1] in right and open_dict[0][:2] not in closed_dict:
        open_dict.append((data[y][x+1], (y, x+1), furthest))
    # check down
    if down in trans[open_dict[0][0]] and y < (len(data)-1) and data[y+1][x] in down and open_dict[0][:2] not in closed_dict:
        open_dict.append((data[y+1][x], (y+1, x), furthest))
    if open_dict[0][:2] not in closed_dict:
        closed_dict.append(open_dict[0][:2])
        closed_distance_dict.append(open_dict[0])
    # print(f"Closed dict: {closed_dict}")
    # print(f"Closed distance dict: {closed_distance_dict}")
    open_dict = open_dict[1:]
    # print(f"Open dict: {open_dict}")
    # print("--------------------")
    # time.sleep(1)

print(closed_distance_dict)
print(closed_distance_dict[-1][2])

min_y = min([tup[1][0] for tup in closed_distance_dict])
max_y = max([tup[1][0] for tup in closed_distance_dict])

