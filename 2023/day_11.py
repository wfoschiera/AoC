from itertools import product, combinations

test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def solution_p1(data):
    galx_c = coord_from_galaxies(data)
    pairs = combinations(galx_c.values(), 2)
    distances = []
    for p1, p2 in pairs:
        distances.append(manhattan_distance(*p1, *p2))
    return distances


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def coord_from_galaxies(data):
    galaxies_coord = dict()
    galx_counter = 1
    for i, line in enumerate(data):
        for j, col in enumerate(line):
            if col == "#":
                galaxies_coord[galx_counter] = (j, i)
                galx_counter += 1
    return galaxies_coord


def expand_the_universe(data):
    data = expand_rows(data)
    data = expand_cols(data)
    return data


def expand_cols(data):
    final = data
    i = 0
    while 1:
        row = ""
        for line in data:
            row += line[i]
        if is_empty(row):
            final = []
            for l in data:
                final.append(l[:i] + "." + l[i:])
            i += 1
        i += 1
        if i >= len(final[0]):
            break
        data = final

    return final


def expand_rows(data):
    final = []
    for line in data:
        final.append(line)
        if is_empty(line):
            final.append(line)
    return final


def is_empty(row_col):
    return set(row_col) == {"."}


if __name__ == '__main__':
    # Part 1
    # Test
    data = test_data.splitlines()
    expanded_data = expand_the_universe(data)
    res = sum(solution_p1(expanded_data))
    print(res)
    assert res == 374

    # Part 1
    # Test
    data = open("day_11.txt").read().splitlines()
    expanded_data = expand_the_universe(data)
    res = sum(solution_p1(expanded_data))
    print(res)
    assert res == 9509330