import re


def is_palindrome(line: str) -> bool:
    word = re.sub(r'\W', '', line.lower())
    return word == word[::-1]


def main():
    print(is_palindrome(input().strip()))


if __name__ == '__main__':
    main()
