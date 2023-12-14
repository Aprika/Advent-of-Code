# seeds: seed types to be planted
# the rest:
#   1. number = start of destination (e.g. soil) range
#   2. number = start of origin (e.g. seed) range
#   3. number = length of range

with open("input_5.txt") as txt:
    data = txt.readlines()
    data = "".join(data)

print(data)

# Set up values:
data_parts = data.split("\n\n")
print(data_parts)
seeds = [int(x) for x in data_parts[0].split(" ")[1:]]
seed_to_soil = [x.split(" ") for x in data_parts[1].split("\n")[1:]]
soil_to_fertilizer = [x.split(" ") for x in data_parts[2].split("\n")[1:]]
fertilizer_to_water = [x.split(" ") for x in data_parts[3].split("\n")[1:]]
water_to_light = [x.split(" ") for x in data_parts[4].split("\n")[1:]]
light_to_temperature = [x.split(" ") for x in data_parts[5].split("\n")[1:]]
temperature_to_humidity = [x.split(" ") for x in data_parts[6].split("\n")[1:]]
humidity_to_location = [x.split(" ") for x in data_parts[7].strip().split("\n")[1:]]

altogether = [seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
              water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
print(altogether)
processes = altogether[1:]
print(processes)

# Idea: create hash tables in the form of dictionaries for each transition
hash_tables = []
for trans in processes:
    print(trans)
    hash_tables.append(dict(sorted({(int(i[1]), int(i[1])+int(i[2])):(int(i[0])-int(i[1])) for i in trans}.items())))

print(f"Hash tables: {hash_tables}")


ranges = []
num = 0
while num < len(seeds):
    ranges.append((seeds[num], seeds[num] + seeds[num+1]))
    num += 2

ranges = sorted(ranges)

print(f"Ranges: {ranges}")
final_ranges = [ranges[:]]

# Current idea: brute force with if else
for trans in hash_tables:
    new_ranges = []
    solutions_found = False
    for rng_min, rng_max in final_ranges[-1]:
        print(f"Current range: {(rng_min, rng_max)}")
        out_of_loop = False
        minimum = rng_min
        print(f"Minimum: {minimum}")
        maximum = rng_max
        print(f"Maximum: {maximum}")
        for idx, key in zip(range(len(trans.keys())), trans.keys()):
            if out_of_loop:
                break
            print(f"Key: {key} with value {trans[key]}")
            while (minimum, maximum) != (None, None):
                # Range of tuple's minimum is in current range
                if minimum in range(key[0], key[1]):
                    print(f"{minimum} in range {key}")
                    # Range of tuple's max also in range = perfectly in range
                    # >>> Shift the whole tuple
                    if maximum in range(key[0], key[1]):
                        new_ranges.append((minimum+trans[key], maximum+trans[key]))
                        print(f"Appended {(minimum+trans[key], maximum+trans[key])}")
                        print("~~~~~~~~~~")
                        minimum = None
                        maximum = None
                        out_of_loop = True
                        break
                    # Range of minimum in range, range of max out of range
                    # >>> Shift bottom part, change tuple min to range upper limit
                    else:
                        new_ranges.append((minimum+trans[key], key[1]+trans[key]))
                        print(f"Appended {(minimum+trans[key], key[1]+trans[key])}")
                        minimum = key[1]
                        print("~~~~~~~~~~")
                # Minimum not in range
                else:
                    print(f"{minimum} not in range {key}")
                    # Minimum is smaller than current range
                    if minimum < key[0]:
                        # Tuple is entirely out of range
                        # >>> Add tuple unchanged
                        if maximum < key[0] or maximum > key[1] and idx == len(trans.keys())-1:
                            new_ranges.append((minimum, maximum))
                            print(f"Appended {(minimum, maximum)}")
                            print("~~~~~~~~~~")
                            minimum = None
                            maximum = None
                        # Maximum in range
                        # >>> Divide into two parts: one unchanged, two changed
                        elif maximum in range(key[0], key[1]):
                            print("Two part divide, min out")
                            new_ranges.append((minimum, key[0]))
                            new_ranges.append((key[0]+trans[key], maximum+trans[key]))
                            print(f"Appended {(minimum, key[0])}")
                            print(f"Appended {(key[0]+trans[key], maximum+trans[key])}")
                            minimum = None
                            maximum = None
                        else:
                            print("Three part divide, min and max out")
                            new_ranges.append((minimum, key[0]))
                            new_ranges.append((key[0]+trans[key], key[1]+trans[key]))
                            print(f"Appended {(minimum, key[0])}")
                            print(f"Appended {(key[0]+trans[key], key[1]+trans[key])}")
                            minimum = key[1]
                    # Minimum is greater than the current range
                    # >>> Continue iterating
                    else:
                        print(f"{minimum} > {key}")
                        if idx == len(trans.keys())-1 and minimum != maximum:
                            new_ranges.append((minimum, maximum))
                            print(f"Appended {(minimum, maximum)}")
                            minimum = None
                            maximum = None
                            continue
                        print("~~~~~~~~~~")
                        break


                print(f"New ranges status: {new_ranges}")
                print("------------------")
    new_ranges = sorted(new_ranges)
    print(new_ranges)
    final_ranges.append(new_ranges)
    print(f"Appended {new_ranges} to final_ranges")
    print("************")

for hashed in zip(hash_tables, final_ranges):
    print(hashed)
print(final_ranges)
print(min(final_ranges[-1])[0])
