def read_word_search(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]


def count_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    count = 0

    def check_direction(i, j, dx, dy):
        """Checking if the word exists in a specific direction starting at (i, j)."""
        for k in range(word_length):
            x, y = i + k * dx, j + k * dy
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != word[k]:
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            if check_direction(i, j, 0, 1):
                count += 1
            if check_direction(i, j, 1, 0):
                count += 1
            if check_direction(i, j, 0, -1):
                count += 1
            if check_direction(i, j, -1, 0):
                count += 1
            if check_direction(i, j, 1, 1):
                count += 1
            if check_direction(i, j, 1, -1):
                count += 1
            if check_direction(i, j, -1, 1):
                count += 1
            if check_direction(i, j, -1, -1):
                count += 1

    return count


def main():

    file_name = 'problem4.txt'
    grid = read_word_search(file_name)

    word = "XMAS"

    total_occurrences = count_occurrences(grid, word)
    print(f"Total occurrences of the word '{word}': {total_occurrences}")


if __name__ == "__main__":
    main()
