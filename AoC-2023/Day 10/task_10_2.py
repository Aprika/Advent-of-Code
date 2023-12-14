with open('example_10.txt') as txt:
    data = txt.readlines()

up = ['|', '7', 'F']
left = ['-', 'L', 'F']
right = ['-', 'J', '7']
down = ['|', 'J', 'L']
trans = {'S': [up, left, right, down], '|': [up, down], '7': [left, down], 'F': [right, down],
         '-': [left, right], 'L': [up, right], 'J': [up, left]}

