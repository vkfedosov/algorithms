def to_binary(number: int) -> str:
    binary = ''
    if number == 0:
        binary = '0'
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary


def read_input() -> int:
    return int(input().strip())


def main():
    print(to_binary(read_input()))


if __name__ == '__main__':
    main()
