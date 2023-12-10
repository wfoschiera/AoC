import re
from math import lcm
from itertools import cycle

test_data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

input_data_p2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


def solution_pt1(data, header, first_node):
    nodes = get_nodes(data)
    return get_steps(first_node, header, nodes)


def get_steps(first_node, header, nodes):
    steps = 0
    actual = first_node
    header = cycle(header)
    while actual != "ZZZ":
        inst = next(header)
        left, right = nodes[actual]
        actual = left if inst == "L" else right
        steps += 1
    return steps


def get_nodes(data):
    nodes = {}
    for line in data:
        key, value = line.split(" = ")
        value = re.findall(r'[\d\w]{3}', value)
        nodes[key] = value
    return nodes


def get_steps_p2(first_node, header, nodes):
    steps = 0
    actual = first_node
    header = cycle(header)
    while actual[-1] != "Z":
        inst = next(header)
        left, right = nodes[actual]
        actual = left if inst == "L" else right
        steps += 1
    return steps


def solution_p2(data, header):
    nodes = get_nodes(data)
    a_nodes = [node for node in nodes if node[-1] == "A"]
    print(len(a_nodes))
    steps = []
    for node in a_nodes:
        steps.append(get_steps_p2(node, header, nodes))
    print(steps)
    return lcm(*steps)


if __name__ == '__main__':
    # Part 1
    # Test
    # header, data = test_data.split("\n\n")
    # data = data.splitlines()
    # res = solution_pt1(data, header, "AAA")
    # print(res)
    # #
    # assert res == 6
    #
    # # Result
    # data = open("day_08.txt").read()
    # header, data = data.split("\n\n")
    # data = data.splitlines()
    # res = solution_pt1(data, header, "AAA")
    # print(res)
    #
    # assert res == 16897

    # PART 2
    # TEST
    header, data = input_data_p2.split("\n\n")
    data = data.splitlines()
    res = solution_p2(data, header)
    print(res)
    assert res == 6

    # Result
    data = open("day_08.txt").read()
    header, data = data.split("\n\n")
    data = data.splitlines()
    res = solution_p2(data, header)
    print(res)
    # # assert res == 6
