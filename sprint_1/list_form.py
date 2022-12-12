from typing import List, Tuple


def get_sum(number_list: int, k: int) -> List[int]:
    summ = number_list + k
    summ_to_str = str(summ)
    str_to_map = map(int, summ_to_str)
    return list(str_to_map)


def read_input() -> Tuple[int, int, int]:
    n = int(input())
    number_list = int(input().replace(' ', ''))
    k = int(input())
    return n, number_list, k


def main():
    n, number_list, k = read_input()
    print(" ".join(map(str, get_sum(number_list, k))))


if __name__ == '__main__':
    main()
