with open("input_4.txt") as txt:
    lines = txt.readlines()

total_sum = 0
init_numbers = [1 for x in range(len(lines))]
mult = dict(zip(range(0, len(lines)), init_numbers))
print(mult.items())
for idx, line in zip(range(len(lines)), lines):
    card_sum = 0
    data = line.split(": ")[1]
    winning = [x for x in data.split(" | ")[0].strip().split(" ") if x]
    have = [x for x in data.split(" | ")[1].strip().split(" ") if x]
    print(f"Winning: {winning}")
    print(f"You have: {have}")
    for num in have:
        if num in winning:
            card_sum += 1
    print(f"Number of wins: {card_sum}")
    for card in range(idx+1, min(idx + 1 + card_sum, len(lines))):
        mult[card] += mult[idx]
    print(mult.items())
    total_sum += card_sum
    print("---------------")

print(sum(mult.values()))
