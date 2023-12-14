with open("input_2.txt") as txt:
    file = txt.readlines()

games_sum = 0

for line in file:
    correct = {"red": 0, "green": 0, "blue": 0}
    no_colon = line.split(": ")
    game_num = int(no_colon[0].split(" ")[1])
    all_games = no_colon[1].split("; ")
    for game in all_games:
        cube_split = game.split(", ")
        for cube in cube_split:
            number = int(cube.split(" ")[0])
            color = cube.split(" ")[1].strip()
            if color in correct.keys():
                if correct[color] < number:
                    print(f"For {color}: {correct[color]} < {number}")
                    correct[color] = number
    power = correct["red"]*correct["green"]*correct["blue"]
    print(f"Power: " + str(power))
    games_sum += power
    print("-----------")


print(games_sum)
