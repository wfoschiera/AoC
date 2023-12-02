def open_files(path):
    data = open(path, "r")
    csv = data.readlines()
    data.close()
    return csv




def extract_left_digit(text):
    for letter in text:
        if letter.isdigit():
            return letter


def extract_right_digit(text):
    for letter in text[::-1]:
        if letter.isdigit():
            return letter


def get_digits(data):
    total = 0
    soma_list = []
    for line_str in data:
        text = line_str.strip()
        # print(f"{text=}")

        left = extract_left_digit(text)
        right = extract_right_digit(text)
        print(f"{left=}, {right=}")
        soma = left + right

        total += int(soma)
        soma_list.append(soma)
        print(f"{soma=}")
    print(soma_list)
    return total


if __name__ == "__main__":
    data = open_files("input.txt")
    extracted = get_digits(data)
    print("extracted= ", extracted)
    print("finished")
