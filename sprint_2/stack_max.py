class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if len(self.max) == 0:
            self.max.append(item)
        elif item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.is_empty():
            return 'None'
        return self.max[-1]

    def is_empty(self):
        return self.items == []


def main():
    n = int(input())

    stack_max = StackMax()
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'push':
            stack_max.push(int(item[1]))
        elif item[0] == 'pop':
            if stack_max.pop() == 'error':
                result.append('error')
        elif item[0] == 'get_max':
            result.append(stack_max.get_max())
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
