class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


# В качестве ответа сдайте только текущую функцию.
# Решение надо отправлять только в виде файла с расширением, которое
# соответствует вашему языку. Иначе даже корректное решение не пройдет тесты.
def solution(node):
    while node:
        print(node.value, end="\n")
        node = node.next_item
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print(solution(node0))


if __name__ == '__main__':
    test()
