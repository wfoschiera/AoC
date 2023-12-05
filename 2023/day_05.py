import functools

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


def parse_input(data):
    maps = {}
    ordered_maps = []
    data = data.split("\n\n")
    for map_ in data:
        name, values = map_.split(":")
        if name == "seeds":
            maps[name] = list(map(int, values.strip().split(" ")))
            continue
        ordered_maps.append(name)
        maps[name] = create_map(values.strip())
    locations = []
    for seed in maps["seeds"]:
        locations.append(get_location(maps, seed, ordered_maps))
    return min(locations)


def get_location(maps, index, ordered_maps):
    if len(ordered_maps) == 1:
        return maps[ordered_maps[0]].get(index, index)
    index = maps[ordered_maps[0]].get(index, index)
    location = get_location(maps, index, ordered_maps[1:])
    return location


def create_map(lines: str) -> dict:
    """
    >>> lines = '''50 98 2
    ... 52 50 48'''
    >>> res = create_map(lines)
    >>> print(res)
    >>> assert isinstance(res,dict)
    """
    map_ = {}
    for line in lines.split("\n"):
        destination, origin, range_ = line.split(" ")
        origin = int(origin)
        destination = int(destination)
        range_ = int(range_)
        origins = range(origin, origin + range_)
        destinations = range(destination, destination + range_)
        for orig, dest in zip(origins, destinations):
            map_[orig] = dest
    return map_


if __name__ == '__main__':
    # PART 1
    # TEST
    # resp = parse_input(data=test_data)
    # print(resp)
    # assert resp == 35

    # RESULT
    data = open("day_05.txt").read()
    resp = parse_input(data=data)
    print(resp)
