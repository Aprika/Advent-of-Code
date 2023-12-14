import re
import time

with open("input_8.txt") as txt:
    data = "".join(txt.readlines())
direct = data.split("\n\n")[0]

network = "".join(data.split("\n\n")[1]).split("\n")
print(network)
start = [line.split(" = ")[0] for line in network]
dest = [re.sub(r"^\W+|\W+$", "", line.split(" = ")[1]).split(", ") for line in network]
start_dest = dict(zip(start, dest))
print(start_dest)

starts = [node for node in start if re.match(r"..A", node)]
current = starts[:]
print(current)
steps = 0

steps_to_z = []
for node in current:
    steps = 0
    while not re.match(r"..Z", node):
        for i in direct:
            steps += 1
            if i == 'L':
                new_node = start_dest[node][0]
            elif i == 'R':
                new_node = start_dest[node][1]
            print(f"{steps} {node} -> {new_node}")
            node = new_node
            # time.sleep(1)
    steps_to_z.append(steps)
    print(steps_to_z)

print(f"Result: {steps}")
