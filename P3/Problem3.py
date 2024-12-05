import re


def extract_and_sum_multiplications(filename):
    with open(filename, 'r') as file:
            data = file.read()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    # Find all matches
    matches = re.findall(pattern, data)

    total_sum = 0
    for match in matches:
        numbers = re.findall(r"\d+", match)
        if len(numbers) == 2:
            x, y = map(int, numbers)
            total_sum += x * y

    return total_sum


def main():
    filename = "problem3.txt"
    result = extract_and_sum_multiplications(filename)
    if result is not None:
        print(f"The sum of all valid multiplications is: {result}")


if __name__ == "__main__":
    main()
