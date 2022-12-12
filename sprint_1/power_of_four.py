def is_power_of_four(number: int) -> bool:
    while True:
        if number == 1:
            return True
        number = number / 4
        if number % 4 > 0 and number != 1:
            return False


def main():
    print(is_power_of_four(int(input())))


if __name__ == '__main__':
    main()
