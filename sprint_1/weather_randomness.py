from typing import Tuple, List


def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            count += 1
    try:
        if temperatures[1]:
            if temperatures[0] > temperatures[1]:
                count += 1
            if temperatures[-2] < temperatures[-1]:
                count += 1
    except Exception:
        count = 1
    return count


def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return n, temperatures


def main():
    n, temperatures = read_input()
    print(get_weather_randomness(temperatures))


if __name__ == '__main__':
    main()
