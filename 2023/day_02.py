from collections import defaultdict

test_data = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


def day_2_solution(data: str, res: dict):
    total = 0
    data = data.strip()
    min_solution = dict()
    for line in data.split("\n"):
        possible = True
        line = line.strip()
        game, result = line.split(":")
        game_num = game.split(" ")[1]
        bags = result.split(";")
        cubes_map = defaultdict(int)
        min_cube = dict(green=0, red=0, blue=0)
        for bag in bags:
            cubes_map = defaultdict(int)
            for c in bag.split(","):
                c = c.strip()
                value, color = c.split(" ")
                cubes_map[color] += int(value)
            for key, value in cubes_map.items():
                min_cube[key] = value if min_cube[key] < value else min_cube[key]
                if cubes_map[key] > res[key]:
                    possible = False
        min_solution[game_num] = min_cube
        if possible:
            total += int(game_num)
    return total, min_solution


def get_power(min_solution):
    total_power = 0
    for game, minimum in min_solution.items():
        power = 1
        for color, value in minimum.items():
            power *= value
        total_power += power
    return total_power


if __name__ == "__main__":
    # part 1
    # TEST
    res = dict(red=12, green=13, blue=14)
    result, _ = day_2_solution(test_data, res)
    assert result == 8
    # FINAL
    data = open("day_02.txt", "r").read()
    result, _ = day_2_solution(data, res)

    # part 2
    # TEST
    _, min_solution = day_2_solution(test_data, res)
    result = get_power(min_solution)
    assert result == 2286

    # FINAL
    total, min_solution = day_2_solution(data, res)
    result = get_power(min_solution)
    print(result)