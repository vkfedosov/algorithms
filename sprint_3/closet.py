from typing import List


def counting_sort(color, n=3):
    if len(color) == 0:
        print(*color)
    counted_values = [0] * n
    counted_values[0] = color.count(0)
    counted_values[1] = color.count(1)
    counted_values[2] = color.count(2)
    i = 0
    for value in range(n):
        for _ in range(0, counted_values[value]):
            color[i] = value
            i += 1
    print(*color)


def read_input() -> List:
    n = int(input())
    color = list(map(int, input().split()))
    return color


def main():
    color = read_input()
    counting_sort(color)


if __name__ == '__main__':
    main()
