import time

with open("input_9.txt") as txt:
    data = txt.readlines()

new_numbers = []

for line in data:
    numbers = [int(x) for x in line.strip().split(" ")][::-1]
    print(line, sep=" ")
    new_list = numbers[:]
    states = [numbers[:]]
    loop_no = 0
    while not set(new_list) == {0}:
        loop_no += 1
        print(" "*loop_no, end="")
        new_list = [new_list[num] - new_list[num-1] for num in range(1, len(new_list))]
        states.append(new_list)
        for num in new_list:
            print(str(num), end=" ")
        print("\n")
        #time.sleep(1)
    create = states[::-1]
    create[0].append(0)
    for c in range(1, len(create)):
        new_num = create[c][-1]+create[c-1][-1]
        create[c].append(new_num)
        print(" "*(len(create)-c-1), end="")
        for num in create[c]:
            print(str(num), end=" ")
        print("\n")
        #time.sleep(1)
    new_numbers.append(new_num)
print(new_numbers)
print(sum(new_numbers))



