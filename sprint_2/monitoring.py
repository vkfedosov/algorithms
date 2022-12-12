from typing import List, Tuple


def transpose_matrix(matrix: List[List[int]], n: int, m: int) -> None:
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = [list(map(int, input().split())) for i in range(n)]
    return matrix, n, m


def main():
    matrix, n, m = read_input()
    transpose_matrix(matrix, n, m)


if __name__ == '__main__':
    main()
