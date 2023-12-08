from collections import Counter, defaultdict
from operator import itemgetter

test_data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def classify_hand(data, pt2=False):
    t_map = {"A":14, "K":13, "Q":12, "J":11, "T":10}
    hand_type = defaultdict(list)

    len_hand_before = 0
    for line in data:
        hand, bid = line.split(" ")
        bid = int(bid)
        hand = [int(t_map.get(char, char)) for char in hand]
        C = Counter(hand)
        sorted(C.items(), key=lambda x: x[1])
        hand_values = C.values()
        def map_hand(hand_values):
            if 5 in hand_values:
                hand_type["five_of_k"].append((hand, bid))

            elif 4 in hand_values:
                if pt2 and C.get(11) == 1:
                    hand_type["five_of_k"].append((hand, bid))
                else:
                    hand_type["four_of_k"].append((hand, bid))

            elif 3 in hand_values:
                if 2 in hand_values:
                    if pt2 and 11 in C:
                        if C.get(11) == 2:
                            hand_type["five_of_k"].append((hand, bid))
                        elif C.get(11) == 1:
                            hand_type["four_of_k"].append((hand, bid))
                    else:
                        hand_type["full"].append((hand, bid))
                else:
                    hand_type["three_of_k"].append((hand, bid))

            elif Counter(hand_values).get(2, 0) == 2:
                if pt2 and 11 in C:
                    hand_type["four_of_k"].append((hand, bid))
                else:
                    hand_type["two_pair"].append((hand, bid))

            elif 2 in hand_values:
                if pt2 and C[11] == 1:
                        hand_type["three_of_k"].append((hand, bid))
                else:
                    hand_type["pair"].append((hand, bid))

            elif list(hand_values) == [1, 1, 1, 1, 1]:
                if pt2 and 11 in C:
                    hand_type["pair"].append((hand, bid))
                else:
                    hand_type["higher"].append((hand, bid))

        map_hand(hand_values)
        len_hand_act = len(hand_type)
        if len_hand_before == len_hand_act:
            print("tá igual", hand, hand_values, bid)
        len_hand_before = len_hand_act

    return hand_type

def sort_hand_types(hand_types) -> dict:
    keys = ["five_of_k",
            "four_of_k",
            "full",
            "three_of_k",
            "two_pair",
            "pair",
            "higher"
            ]
    keys.reverse()
    for key in keys:
        hand_types[key].sort(key=itemgetter(0))
    total = 0
    rank = 1
    for key in keys:
        # print(f"\n\n{key=}")
        for item in hand_types[key]:
            # print(f"{rank=}")
            # print(f"{item=}")
            res = rank * item[1]
            # print(f"{rank=} * {item[1]}")

            total += res
            # print(f"{total=}")
            rank += 1

    return total


def solution_p1(data):
    hand_types = classify_hand(data)
    return sort_hand_types(hand_types)


def solution_p2(data):
    hand_types = classify_hand(data, True)
    return sort_hand_types(hand_types)


if __name__ == '__main__':
    # Part 1
    # TEST
    data = test_data.splitlines()
    res = solution_p1(data)
    print(res)
    assert res == 6440

    # Result
    data = open("day_07.txt").read().splitlines()
    res = solution_p1(data)
    print(res)
    assert res == 248812215

    # Part 2
    # TEST
    data = test_data.splitlines()
    res = solution_p2(data)
    print(res)
    assert res == 5905

    # Result
    data = open("day_07.txt").read().splitlines()
    res = solution_p2(data)
    print(res)
