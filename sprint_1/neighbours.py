from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], y: int, x: int) -> List[int]:
    result = []
    if y + 1 < len(matrix):
        result.append(matrix[y + 1][x])
    if x + 1 < len(matrix[0]):
        result.append(matrix[y][x + 1])
    if y - 1 >= 0:
        result.append(matrix[y - 1][x])
    if x - 1 >= 0:
        result.append(matrix[y][x - 1])

    result.sort()
    return result


def read_input() -> Tuple[int, List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    y = int(input())
    x = int(input())
    return m, matrix, y, x


def main():
    m, matrix, y, x = read_input()
    print(" ".join(map(str, get_neighbours(matrix, y, x))))


if __name__ == '__main__':
    main()
