from itertools import pairwise

input_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def solution_pt1(data):
    estimated_num = []
    for line in data:
        values = [int(x) for x in line.split(" ")]
        # print(values)
        cycles = get_zeros(values)
        estimated_num.append(estimate(cycles))

    return estimated_num

def solution_pt2(data):
    estimated_num = []
    s_lines = 0
    for line in data:
        s_lines += 1
        values = [int(x) for x in line.split(" ")]

        # print(values)
        cycles = get_zeros(values)
        estimated_num.append(estimate_p2(cycles))
    print(len(estimated_num))
    est = [proj[-1][0] for proj in estimated_num]
    print(s_lines)
    return est


def get_zeros(numbers, last_list=None):
    if last_list is None:
        last_list = []
    last_list.insert(0, numbers)
    # Nao pode ser soma pq [1, -1] é falso positivo.
    if set(numbers) == {0}:
        return last_list

    new_iter = [b - a for a, b in pairwise(numbers)]

    return get_zeros(new_iter, last_list)

def estimate(cycles):
    # cycles = [[0, 0, 0, 0], [3, 3, 3, 3, 3], [0, 3, 6, 9, 12, 15]]
    for cur_item, next_item in pairwise(cycles):
        input_ = next_item[-1] + cur_item[-1]
        next_item.append(input_)
    return input_

def estimate_p2(cycles):
    for cur_item, next_item in pairwise(cycles):
        next_item.insert(0, next_item[0] - cur_item[0])

    return cycles


if __name__ == '__main__':
    # PART 1
    # TEST
    data = input_data.split("\n")
    res = solution_pt1(data)
    print(res)
    print(sum(res))

    # # RESULT
    data = open("day_09.txt").read().splitlines()
    res = sum(solution_pt1(data))
    print(res)
    assert res == 1772145754

    # PART 2
    # TEST
    data = input_data.split("\n")
    res = sum(solution_pt2(data))
    print(res)
    assert res == 2
    #
    # # RESULT
    data = open("day_09.txt").read().splitlines()
    res = sum(solution_pt2(data))
    print(res)
    assert res == 867
