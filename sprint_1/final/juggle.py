from typing import List, Tuple


def get_max_points(matrix: List[str], k: int) -> int:
    points = 0
    count = [0] * 16
    for number in matrix:
        if number != '.':
            count[int(number)] += 1
    for number in count:
        if 0 < number <= k * 2:
            points += 1
    return points


def read_input() -> Tuple[List[str], int]:
    k = int(input())
    matrix = [i for i in range(4) for i in input().strip()]
    return matrix, k


def main():
    matrix, k = read_input()
    print(get_max_points(matrix, k))


if __name__ == '__main__':
    main()
