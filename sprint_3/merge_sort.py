from typing import List


def merge(arr: list, lf: int, mid: int, rg: int) -> List:
    result = []
    left = arr[lf:mid]
    right = arr[mid:rg]
    i_left = i_right = 0
    while len(result) < len(left) + len(right):
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
        if i_right == len(right):
            result += left[i_left:]
            break
        if i_left == len(left):
            result += right[i_right:]
            break
    return result


def merge_sort(arr: list, lf: int, rg: int) -> None:
    if rg - lf >= 2:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        arr[lf:rg] = merge(arr, lf, mid, rg)


def main():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    main()
