import re

with open("input_1.txt") as txt:
    all_lines = txt.readlines()

print(all_lines[:10])

str_nums = re.compile("one|two|three|four|five|six|seven|eight|nine")
str_to_nums = {"one": "on1e", "two": "tw2o", "three": "thr3ee", "four": "fou4r", "five": "fi5ve", "six": "si6x",
               "seven": "sev7en", "eight": "eigh8t", "nine": "nin9e"}

matches = list(zip(all_lines, [str_nums.findall(line) for line in all_lines]))
print(matches[:10])

pre_cleaned = []
for line in matches:
    origin, string = line
    for option in str_to_nums.keys():
        origin = re.sub(option, str_to_nums[option], origin)
    pre_cleaned.append(origin)

print(pre_cleaned[:10])


# pre_cleaned = [[[re.sub(option, str_to_nums[option], origin) for option in string]
#               for origin, string in line] for line in matches]


cleaned = [re.sub(r"\D", "", line) for line in pre_cleaned]
print(cleaned[:10])
first_last = [int(digit[0]+digit[-1]) for digit in cleaned]
print(first_last[:10])

print(sum(first_last[:10]))
print(sum(first_last))
