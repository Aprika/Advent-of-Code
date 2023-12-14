import re

with open("input_3.txt") as txt:
    data = txt.readlines()

for line in data:
    print(len(line))
    break

# numbers = re.compile("\d+")
# symbols = re.compile("")
numbers_dict = {}
symbols_dict = {}

# collect all numbers, symbols and their indices
for idx_y, line in zip(range(len(data)), data):
    is_digit = False
    number = ""
    num_range_start = 0
    max_x = len(line)
    max_y = len(data)
    for idx_x, symbol in zip(range(len(line)), line):
        if symbol.isdigit():
            print(f"Symbol {symbol} is a digit")
            if not is_digit:
                is_digit = True
                num_range_start = idx_x
            number += symbol

        elif is_digit:
            print(f"Symbol {symbol} is not a digit, but previous was digit")
            if not numbers_dict.get(number):
                print(f"Added number {number}")
                numbers_dict[number] = [((num_range_start, idx_x), idx_y)]
            else:
                print(f"Added new location for existing number {number}")
                numbers_dict[number].append(((num_range_start, idx_x), idx_y))
            is_digit = False
            number = ""
            num_range_start = 0

        if symbol == "*":
            print(f"Symbol {symbol} is a special character")
            if not symbols_dict.get(symbol):
                symbols_dict[symbol] = [(idx_x, idx_y)]
            else:
                symbols_dict[symbol].append((idx_x, idx_y))

print("Number dictionary:" + str(numbers_dict.items()))
print("Symbol dictionary:" + str(symbols_dict.items()))

all_symbol_indices = []
for locs in symbols_dict.values():
    all_symbol_indices.extend(locs)

print("Symbol values: " + str(all_symbol_indices))

all_gears = []


for symbol in all_symbol_indices:
    num_adj = 0
    adj_numbers = []
    # exit = False
    print(f"Current gear: {symbol}")
    for number, idx in numbers_dict.items():
        for this_range in idx:
            max_x = len(data[0])
            x_range = range(max(0, this_range[0][0]-1), min(max_x, this_range[0][1]+1))
            y_range = range(max(0, this_range[1]-1), min(len(data), this_range[1]+2))
            print(f"For number {number}: x range = {x_range}, y range = {y_range}")
            if symbol[0] in x_range and symbol[1] in y_range:
                print(f"Number {number} is in range")
                num_adj += 1
                adj_numbers.append(number)
    if num_adj == 2:
        all_gears.append(adj_numbers)
    print("----------")

print(f"All gears: {all_gears}")

prod_sum = sum([int(gear[0]) * int(gear[1]) for gear in all_gears])

print(prod_sum)

