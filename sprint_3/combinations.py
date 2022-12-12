LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def gen_binary(buttons, path, result):
    if buttons == '':
        result.append(path)
        return
    for letter in LETTERS[buttons[0]]:
        path += letter
        gen_binary(buttons[1:], path, result)
        path = path[:-1]


def read_input() -> str:
    buttons = input()
    return buttons


def main():
    buttons = read_input()
    result = []
    gen_binary(buttons, '', result)
    for x in result:
        print(x, end=' ')


if __name__ == '__main__':
    main()
