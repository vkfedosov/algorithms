from typing import List, Tuple


def moving_average(timeseries: List[int], k: int) -> List[float]:
    result = []
    current_sum = sum(timeseries[0:k])
    result.append(current_sum / k)
    for i in range(0, len(timeseries) - k):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + k]
        current_avg = current_sum / k
        result.append(current_avg)
    return result


def read_input() -> Tuple[int, List[int], int]:
    n = int(input())
    timeseries = list(map(int, input().strip().split()))
    k = int(input())
    return n, timeseries, k


def main():
    n, timeseries, k = read_input()
    print(" ".join(map(str, moving_average(timeseries, k))))


if __name__ == '__main__':
    main()
