from typing import List


def factorize(number: int) -> List[int]:
    result = []
    div = 2
    while div ** 2 <= number:
        if number % div == 0:
            number //= div
            result.append(div)
        else:
            div += 1
    if number > 1:
        result.append(number)
    return result


def main():
    print(" ".join(map(str, factorize(int(input())))))


if __name__ == '__main__':
    main()
