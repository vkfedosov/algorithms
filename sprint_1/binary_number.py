from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    if len(first_number) > len(second_number):
        first_number, second_number = second_number, first_number

    first_number = '0' * (
            len(second_number) - len(first_number)) + first_number
    add_one = 0
    result = ''
    for i in range(len(second_number) - 1, -1, -1):
        s = int(first_number[i]) + int(second_number[i]) + add_one
        add_one, s = divmod(s, 2)
        result += str(s)
    if add_one == 1:
        result += '1'
    return result[::-1]


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


def main():
    first_number, second_number = read_input()
    print(get_sum(first_number, second_number))


if __name__ == '__main__':
    main()
