test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
data = test_data.split("\n")


def num_with_adj_sym(data: str):
    total = []
    lines = {}
    for i, line in enumerate(data):
        lines[i] = line

    for line_num, line in lines.items():
        line = line.strip()
        num = ""
        flag = False
        for pos, char in enumerate(line):
            if char.isdigit():
                if not flag:
                    start_pos = pos
                flag = True
                num += char
                if pos == 139:
                    if has_adj_sym(num, start_pos, line_num, lines):
                        total.append(int(num))
            else:
                if num == "":
                    continue
                if has_adj_sym(num, start_pos, line_num, lines):
                    total.append(int(num))
                num = ""
                flag = False

    return total


def has_adj_sym(number: str, start_pos: int, line_num: int, lines: dict):
    pos_start = start_pos
    pos_end = pos_start + len(number)
    num_line_above = line_num - 1 if line_num > 0 else line_num
    num_line_below = line_num + 1 if line_num < len(lines) - 1 else line_num
    line_above = lines[num_line_above]
    line_target = lines[line_num]
    line_below = lines[num_line_below]
    max_index = len(line_target) - 1
    low_index = 0

    left_limit = max(pos_start - 1, low_index)
    right_limit = min(pos_end + 1, max_index) if pos_end < 140 else -1

    line_target = line_target[left_limit: right_limit].replace(number, "")
    line_above = line_above[left_limit: right_limit].replace(number, "")
    line_below = line_below[left_limit: right_limit].replace(number, "")

    symbols = (line_target + line_above + line_below).strip(".123456789")
    return bool(symbols)


if __name__ == '__main__':
    # PART 1
    # TEST
    # list_total = num_with_adj_sym(data)
    # print(list_total)
    # print(sum(list_total))
    # 4361
    # Result
    data = open("day_03.txt")
    _, lista = p1(data)
    print(lista)
    print(sum(lista))
    # # # print(data)
    data = open("day_03.txt")
    list_total = num_with_adj_sym(data.readlines())
    print("Meu resultado errado")
    print(list_total)
    print(f"Result: ", sum(list_total))

# 513825