from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    for i in longer:
        if i in shorter:
            shorter = shorter.replace(i, '', 1)
        else:
            return i


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


def main():
    shorter, longer = read_input()
    print(get_excessive_letter(shorter, longer))


if __name__ == '__main__':
    main()
