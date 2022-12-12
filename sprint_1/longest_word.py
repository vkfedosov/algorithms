def get_longest_word(line: str) -> str:
    word = line.split()
    return max(word, key=len)


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


def main():
    print_result(get_longest_word(read_input()))


if __name__ == '__main__':
    main()
