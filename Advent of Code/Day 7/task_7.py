from collections import defaultdict

with open("input_7.txt") as txt:
    data = txt.readlines()

prio_dict = {14: "A", 13: "K", 12: "Q", 1: "J", 10: "T"}

prio_dict.update(dict(zip(range(2, 10), [str(x) for x in range(2, 10)])))
prio_dict = dict(reversed(sorted(prio_dict.items())))
prio_dict = {val: key for key, val in prio_dict.items()}


cards = [line.split(" ")[0] for line in data]
bets = [int(line.strip().split(" ")[1]) for line in data]

card_to_bets = dict(zip(cards, bets))


def wordcount(my_list):
    word_count = defaultdict(int)
    for word in my_list:
        word_count[word] += 1
    return word_count


all_values = [wordcount(card).values() for card in cards]

# 3 in wordcount(card).values() and 2 in wordcount(card).values()
five_of = [card for card in cards if max(wordcount(wordcount(card.replace("J", "")+"R").values())) + wordcount(card)["J"] >= 5]
four_of = [card for card in cards if max((wordcount(card.replace("J", "")+"R").values())) + wordcount(card)["J"] == 4]
three_of = [card for card in cards if max(wordcount(card.replace("J", "")+"R").values()) + wordcount(card)["J"] == 3
            and len(wordcount(card.replace("J", "")).values()) > 2]
one_pair = [card for card in cards if max(wordcount(wordcount(card).values())) + wordcount(card)["J"] == 2
            and wordcount(wordcount(card).values())[2] <= 1]
two_pair = [card for card in cards if max(wordcount(wordcount(card).values())) + wordcount(card)["J"] == 2
            and card not in one_pair]
full_house = [card for card in cards if max(wordcount(wordcount(card).values())) + wordcount(card)["J"] == 3
              and card not in three_of]
high_card = [card for card in cards if max(wordcount(wordcount(card).values())) + wordcount(card)["J"] == 1]

all_types = [high_card, one_pair, two_pair, three_of, full_house, four_of, five_of]
print(f"High cards: {all_types[0]}")
print(f"One pair: {all_types[1]}")
print(f"Two pair: {all_types[2]}")
print(f"Three of: {all_types[3]}")
print(f"Full house: {all_types[4]}")
print(f"Four of: {all_types[5]}")
print(f"Five of: {all_types[6]}")

re_sorted = []
for this_type in all_types:
    new_dict = {}
    for val in this_type:
        new_dict[val] = [prio_dict[x] for x in val]
    sorted_dict = {}
    sorted_keys = sorted(new_dict, key=new_dict.get)

    for w in sorted_keys:
        sorted_dict[w] = new_dict[w]
    re_sorted.extend(sorted_dict.keys())


points = dict(zip(re_sorted, range(1, len(re_sorted) + 1)))

print(points)

result = sum([rank * card_to_bets[cards] for cards, rank in points.items()])
print(result)
