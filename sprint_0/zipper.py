from typing import List, Tuple


def zipper(a: List[int], b: List[int], n: int) -> List[int]:
    zipper = []
    for i in range(n):
        zipper.append(a[i])
        zipper.append(b[i])
    return zipper


def read_input() -> Tuple[List[int], List[int], int]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b, n


def main():
    a, b, n = read_input()
    print(" ".join(map(str, zipper(a, b, n))))


if __name__ == '__main__':
    main()
