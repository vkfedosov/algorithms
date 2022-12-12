class Stack:
    def __init__(self):
        self.queue = []

    def get(self):
        if self.is_empty():
            return 'error'
        else:
            return self.queue.pop(0)

    def put(self, item):
        self.queue.append(item)
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


def main():
    n = int(input())

    stack = Stack()
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'get':
            result.append(stack.get())
        elif item[0] == 'size':
            result.append(stack.size())
        elif item[0] == 'put':
            stack.put(int(item[1]))

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
