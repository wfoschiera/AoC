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


def solution(data, empty_rows, empty_cols, exp_factor=1):
    galx_c = coord_from_galaxies(data)
    pairs = combinations(galx_c.values(), 2)
    distances = []
    for p1, p2 in pairs:
        distance = expanded_distance(*p1, *p2, empty_rows, empty_cols, exp_factor)
        distances.append(distance)
    return distances


def expanded_distance(x1, y1, x2, y2, empty_rows, empty_cols, factor):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    start_x = min(x1, x2)
    start_y = min(y1, y2)

    stop_x = start_x + dx
    stop_y = start_y + dy

    range_cols = set(range(start_x, stop_x + 1))
    range_rows = set(range(start_y, stop_y + 1))

    x_dim = range_cols.intersection(empty_cols)
    y_dim = range_rows.intersection(empty_rows)

    dx += sum([factor for exp in x_dim])
    dy += sum([factor for exp in y_dim])

    return dx + dy


def coord_from_galaxies(data):
    galaxies_coord = dict()
    galx_counter = 1
    for i, line in enumerate(data):
        for j, col in enumerate(line):
            if col == "#":
                galaxies_coord[galx_counter] = (j, i)
                galx_counter += 1
    return galaxies_coord
#
#
# def expand_the_universe(data):
#     data = expand_rows(data)
#     data = expand_cols(data)
#     return data


def empty_cols(data):
    final = set()
    for i in range(len(data[0])):
        row = ""
        for line in data:
            row += line[i]
        if is_empty(row):
            final.add(i)
    return final


def empty_rows(data):
    final = set()
    for i, line in enumerate(data):
        if is_empty(line):
            final.add(i)
    return final


def is_empty(row_col):
    return set(row_col) == {"."}


if __name__ == '__main__':
    # # Part 1
    # # Test
    # data = test_data.splitlines()
    # e_r = empty_rows(data)
    # e_c = empty_cols(data)
    # # expanded_data = expand_the_universe(data)
    # res = sum(solution(data, e_r, e_c))
    # print(res)
    # assert res == 374
    #
    # # Part 1
    # # Test
    # data = open("day_11.txt").read().splitlines()
    # e_r = empty_rows(data)
    # e_c = empty_cols(data)
    # # expanded_data = expand_the_universe(data)
    # res = sum(solution(data, e_r, e_c))
    # print(res)
    # assert res == 9509330

    # Part 2
    # Test
    data = test_data.splitlines()
    e_r = empty_rows(data)
    e_c = empty_cols(data)
    # expanded_data = expand_the_universe(data)
    res = sum(solution(data, e_r, e_c, exp_factor=9))
    print(res)
    assert res == 1030
    # Test 2
    res = sum(solution(data, e_r, e_c, exp_factor=99))
    print(res)
    assert res == 8410

    # Part 2
    # Result
    data = open("day_11.txt").read().splitlines()
    e_r = empty_rows(data)
    e_c = empty_cols(data)
    # expanded_data = expand_the_universe(data)
    res = sum(solution(data, e_r, e_c, exp_factor=999_999))
    print(res)
    assert res == 635832237682