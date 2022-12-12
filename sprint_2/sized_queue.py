class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, item):
        if self.size != self.max_size:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            return 'ok'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def is_empty(self):
        return self.size == 0


def main():
    n = int(input())
    max_size = int(input())

    stack = MyQueueSized(max_size)
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'push':
            if stack.push(int(item[1])) == 'error':
                result.append('error')
        elif item[0] == 'pop':
            result.append(stack.pop())
        elif item[0] == 'peek':
            result.append(stack.peek())
        elif item[0] == 'size':
            result.append(stack.size)

    for i in result:
        print(i)


if __name__ == '__main__':
    main()
