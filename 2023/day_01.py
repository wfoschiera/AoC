from collections.abc import Iterable
from pathlib import Path

INPUT = Path(__file__).with_suffix(".txt")

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
int_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
translate_number = {string: number for string, number in zip(nums, int_numbers)}


def extract_digit(text: str) -> str:
    for letter in text:
        if letter.isdigit():
            return letter


def str_to_int(text: str, dic: dict[str, int]) -> list:
    resp = []
    for i, v in enumerate(text):
        if v.isdigit():
            resp.append(v)
            continue
        for num, digit in dic.items():
            if text[i:].startswith(num):
                resp.append(digit)
                break
    return resp


def get_digits(data: Iterable, part_2: bool = False):
    total = 0
    for line_str in data:
        text = line_str.strip()
        if part_2:
            text = str_to_int(text, translate_number)
            # quando todo mundo é digito, só preciso pegar o primeiro e o ultimo
            # otimizacao boba pra parte 2.
            left, right = text[0], text[-1]
        else:
            left = extract_digit(text)
            right = extract_digit(text[::-1])
        concat = left + right
        total += int(concat)
    return total


if __name__ == "__main__":
    data = INPUT.read_text().splitlines(keepends=True)
    print(get_digits(data))
    print(get_digits(data, True))
