import functools
from collections import OrderedDict

test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def parse_input(data, p2=False):
    seeds, *data = data.split("\n\n")
    seeds = seeds.split(": ")[1]
    seeds = [int(x) for x in seeds.split()]
    return seeds, data

def solution_p1(seeds, parsed_data):
    for map_ in parsed_data:
        _, *values = map_.splitlines()
        ranges = create_map(values)
        def get_next(seed):
            for o, d in ranges:
                if seed in o:
                    return d.start - o.start + seed
            return seed
        seeds = [get_next(seed) for seed in seeds]
    return min(seeds)


def create_map(lines: str) -> set[tuple]:
    map_ = set()
    for line in lines:
        ranges = [int(x) for x in line.split(" ")]
        destinations = range(ranges[0], ranges[0] + ranges[2])
        origins = range(ranges[1], ranges[1] + ranges[2])
        map_.add((origins, destinations))
        del ranges, destinations, origins
    return map_

def solution_p2():
    def pairs(seeds):
        _pairs = set()
    for i, seed in enumerate(seeds):
        if i % 2 == 0:
            _pairs.add((seed, seeds[i + 1]))
    print(_pairs)
    return _pairs


    result = []
    seeds_range = [range(a, a + b) for a, b in pairs(seeds)]
    print(seeds_range)



if __name__ == '__main__':
    # PART 1
    # TEST
    seeds, data = parse_input(data=test_data)
    resp = solution_p1(seeds, data)
    print(resp)
    # assert resp == 35

    # RESULT
    data = open("day_05.txt").read()
    seeds, data = parse_input(data=data)
    resp = solution_p1(seeds, data)
    print(resp)

    # PART 2
    # # TEST
    # resp = parse_input(data=test_data, p2=True)
    # print(resp)
    # assert resp == 46

    # RESULT
    # data = open("day_05.txt").read()
    # resp = parse_input(data=data, p2=True)
    # print(resp)
