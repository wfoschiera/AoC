test_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
test_data = test_data.split("\n")

def clean_data(data):
    cleaned = []
    for line in data:
        line = line.strip()
        line = line.replace("  ", " ")
        line = line.split(": ")[1]
        have, winn = line.split(" | ")
        have = have.split(" ")
        winn = winn.split(" ")
        have = {int(x) for x in have}
        winn = {int(x) for x in winn}
        cleaned.append((have, winn))
    return cleaned


def get_power(cleaned_data):
    powers = {}
    for i, (have, winn) in enumerate(cleaned_data):
        powers[i]= len(have.intersection(winn))
    return powers


def get_result(data):
    total = 0
    cleaned_data = clean_data(data)
    powers = get_power(cleaned_data)
    print(powers)
    for pow in powers.values():
        if pow > 0:
            res = 1
            while pow > 1:
                res *= 2
                pow -= 1
            total += res
    return total


def get_result_p2(data):
    cleaned_data = clean_data(data)
    powers = get_power(cleaned_data)
    instances = {}
    for card_num, pow in powers.items():
        next_card = card_num + 1
        for p in range(1, pow + 1):
            next_card += 1
            if p in powers:
                instances[next_card] = instances.get(next_card, 0) + 1
    return instances

def recur(card_powers, card_num):
    card_powers[card_num] = card_powers.get(card_num, 0) + 1
    return card_powers[card_num]


instances = {0: 1, 1: 2, 2: 4, 3: 8, 4: 14, 5: 1}
total = sum(instances.values())

if __name__ == '__main__':
    # Part 1
    # Test data
    result = get_result(test_data)
    print(result)
    # Part 1
    # Final
    # data = open("day_04.txt").readlines()
    # result = get_result(data)
    # print(result)

    # Part 2
    # Test data
    result = get_result_p2(test_data)
    print(result)
    # Part 2
    # Final
    # data = open("day_04.txt").readlines()
    # result = get_result_p2(data)
    # print(result)