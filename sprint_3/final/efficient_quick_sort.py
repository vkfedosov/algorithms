from typing import List


def quicksort(users: list, lf: int, rg: int) -> int:
    if lf >= rg:
        return -1

    left, right = lf, rg
    pivot = users[lf]

    while left <= right:
        while users[left] < pivot:
            left += 1
        while users[right] > pivot:
            right -= 1
        if left <= right:
            users[left], users[right] = users[right], users[left]
            left += 1
            right -= 1

    quicksort(users, lf, right)
    quicksort(users, left, rg)


def data_sort(users: list) -> List:
    users[1] = -int(users[1])
    users[2] = int(users[2])
    return [users[1], users[2], users[0]]


def read_input() -> List:
    n = int(input())
    users = [data_sort(input().split()) for _ in range(n)]
    return users


def main():
    users = read_input()
    quicksort(users, lf=0, rg=len(users) - 1)
    for username in users:
        print(username[2])


if __name__ == '__main__':
    main()
