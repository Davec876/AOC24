def is_safe_report(report):
    levels = list(map(int, report.split()))

    # func checking if the levels are safe
    def check_safety(levels):
        differences = []
        for x in range(len(levels) - 1):
            differences.append(levels[x + 1] - levels[x])
        return (
                all(1 <= diff <= 3 for diff in differences) or
                all(-3 <= diff <= -1 for diff in differences)
        )

    if check_safety(levels):
        return True

    # Looping through all possible combinations of levels
    for i in range(len(levels)):
        if check_safety(levels[:i] + levels[i + 1:]):
            return True

    return False

def count_safe_reports(filename):
    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            if is_safe_report(line.strip()):
                safe_count += 1
    return safe_count


def main():
    filename = "problem2.txt"
    try:
        safe_reports = count_safe_reports(filename)
        print(f"Number of safe reports: {safe_reports}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
