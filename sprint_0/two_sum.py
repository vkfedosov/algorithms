from typing import List, Tuple, Optional


def two_sum(numbers: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return numbers[i], numbers[j]


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    numbers = list(map(int, input().strip().split()))
    target_sum = int(input())
    return n, numbers, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


def main():
    n, numbers, target_sum = read_input()
    print_result(two_sum(numbers, target_sum))


if __name__ == '__main__':
    main()
