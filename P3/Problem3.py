import re


def extract_and_sum_multiplications(filename):
    with open(filename, 'r') as file:
            data = file.read()

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    matches = re.findall(f"{pattern}|{do_pattern}|{dont_pattern}", data)

    mul_enabled = True
    total_sum = 0

    for instruction in matches:
        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        elif mul_enabled and instruction.startswith("mul("):
            x, y = map(int, re.findall(r"\d+", instruction))
            total_sum += x * y

    return total_sum


def main():
    filename = "problem3.txt"
    result = extract_and_sum_multiplications(filename)
    if result is not None:
        print(f"The sum of all valid multiplications is: {result}")


if __name__ == "__main__":
    main()
