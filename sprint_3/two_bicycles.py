from typing import Tuple, List


def binary_search(money, price, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if money[mid] >= price > money[mid - 1] or mid == 0:
        return mid + 1
    elif money[mid] >= price:
        return binary_search(money, price, left, mid)
    else:
        return binary_search(money, price, mid + 1, right)


def read_input() -> Tuple[int, List[int], int]:
    days = int(input())
    money = list(map(int, input().strip().split()))
    price = int(input())
    return days, money, price


def main():
    days, money, price = read_input()
    print(binary_search(money, price, left=0, right=days), end=' ')
    print(binary_search(money, price * 2, left=0, right=days), end=' ')


if __name__ == '__main__':
    main()
