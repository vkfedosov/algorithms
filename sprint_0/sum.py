from typing import Tuple


def read_inputs() -> Tuple[int, int]:
    a = int(input())
    b = int(input())
    return a, b


def get_sum(a: int, b: int):
    return a + b


def main():
    a, b = read_inputs()
    print(get_sum(a, b))


if __name__ == '__main__':
    main()
