from utils import read_files

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
int_numbers = "1 2 3 4 5 6 7 8 9".split(" ")
translate_number = {string: number for string, number in zip(nums, int_numbers)}


def extract_digit(text):
    # regex.match(all_numbers).groups()
    for letter in text:
        if letter.isdigit():
            return letter


def str_to_int(text, dic):
    resp = []
    for i, v in enumerate(text):
        if v.isdigit():
            resp.append(v)
            continue
        for num in dic.keys():
            print(num)
            if text[i:].startswith(num):
                resp.append(dic[num])
    return resp


def get_digits(data):
    total = 0
    for line_str in data:
        text = line_str.strip()
        text = str_to_int(text, translate_number)

        left = extract_digit(text)
        right = extract_digit(text[::-1])

        concat = left + right
        total += int(concat)
    return total


if __name__ == "__main__":
    data = read_files("input.txt")
    extracted = get_digits(data)
