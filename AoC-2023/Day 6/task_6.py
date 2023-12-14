import re

with open("input_6.txt") as txt:
    data = txt.readlines()

nums = re.compile("\d+")

times = "".join(nums.findall(data[0]))
dists = "".join(nums.findall(data[1]))

print(times)
print(dists)

all_poss = []
poss = len([x for x in range(int(times)) if (int(times)-x)*x > int(dists)])


print(poss)
