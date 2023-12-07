import re

test_data = """Time:      7  15   30
Distance:  9  40  200"""


def parse_data(data):
    time, distance = data.splitlines()
    time = [int(x) for x in re.findall("\d+", time)]
    distance = [int(x) for x in re.findall("\d+", distance)]
    return time, distance



def solution(data):
    ts, ds = parse_data(data)
    total_wins = 1
    # for every race
    for t, d in zip(ts, ds):
        total_wins *= get_total_wins(t, d)

    return total_wins


def get_total_wins(total_time, record):
    total = 0
    has_won = False
    for t in range(total_time):
        dist = (t*1) * (total_time - t)
        if dist > record:
            total += 1
            has_won = True
        elif has_won:
            break
    return total


def solution_2(data):
    ts, ds = parse_data_2(data)
    total_wins = 1
    # for every race
    for t, d in zip(ts, ds):
        total_wins *= get_total_wins(t, d)

    return total_wins


def parse_data_2(data):
    time, distance = data.splitlines()
    time = re.sub(" ", "", time)
    distance = re.sub(" ", "", time)
    return time, distance


if __name__ == '__main__':
    # PT 1
    # TEST
    res = solution(test_data)
    print(res)

    # SOLUTION
    data = open("day_06.txt").read()
    res = solution(data)
    print(res)

    # PT 2
    # TEST
    res = solution_2(test_data)
    print(res)

    # SOLUTION
    data = open("day_06.txt").read()
    res = solution(data)
    print(res)