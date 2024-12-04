from collections import Counter

def calculate_total_distance(left_list, right_list):
    left_list_sorted = sorted(left_list)
    right_list_sorted = sorted(right_list)

    total_distance = sum(abs(l - r) for l, r in zip(left_list_sorted, right_list_sorted))
    return total_distance


def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    similarity_score = sum(num * right_count[num] for num in left_list)
    return similarity_score


def read_lists_from_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into two integers
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list


def main():

    file_path = 'problem1.txt'
    left_list, right_list = read_lists_from_file(file_path)

    # Calculate the total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print("Total Distance:", total_distance)

    # Calculate sim score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print("Similarity Score:", similarity_score)


if __name__ == "__main__":
    main()
