from typing import List


def comparator(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    else:
        sum_1 = number_1 + number_2
        sum_2 = number_2 + number_1
        return sum_1 > sum_2


def bigger_number(numbers, comparator):
    for i in range(len(numbers)):
        item = numbers[i]
        while i > 0 and comparator(item, numbers[i - 1]):
            numbers[i] = numbers[i - 1]
            i -= 1
        numbers[i] = item
    return numbers


def read_input() -> List:
    _ = int(input())
    numbers = [x for x in input().split()]
    return numbers


def main():
    numbers = read_input()
    print(''.join(bigger_number(numbers, comparator)))


if __name__ == '__main__':
    main()
