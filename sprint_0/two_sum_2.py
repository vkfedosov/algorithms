from typing import List, Tuple, Optional


def two_sum(numbers: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    numbers.sort()

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target_sum:
            return numbers[left], numbers[right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1


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
