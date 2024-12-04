def is_safe_report(report):
    levels = list(map(int, report.split()))
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    if increasing := all(1 <= diff <= 3 for diff in differences):
        return increasing
    if decreasing := all(-3 <= diff <= -1 for diff in differences):
        return decreasing

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
