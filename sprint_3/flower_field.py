from typing import Tuple, List


def flower_field(n, field):
    field.sort()
    result = []
    i = 0
    start, end = field[i]
    while i < n:
        if start <= field[i][0] <= end:
            _, curr_end = field[i]
            i += 1
            if curr_end > end:
                end = curr_end
        else:
            result.append([start, end])
            start, end = field[i]
            i += 1
    result.append([start, end])

    for res in result:
        print(*res)


def read_input() -> Tuple[int, List[List[int]]]:
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]
    return n, field


def main():
    n, field = read_input()
    flower_field(n, field)


if __name__ == '__main__':
    main()
