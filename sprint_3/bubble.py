from typing import List


def bubble_sort(array):
    sorted_array = False
    sorted_already = False
    while True:
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted_array = True
                sorted_already = True
        if sorted_array:
            print(' '.join(str(i) for i in array))
            sorted_array = False
        else:
            break
    if not sorted_already:
        print(' '.join(str(i) for i in array))


def read_input() -> List:
    n = int(input())
    array = list(map(int, input().split()))
    return array


def main():
    array = read_input()
    bubble_sort(array)


if __name__ == '__main__':
    main()
