class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node):
    while node:
        print(node.value, end=" -> ")
        node = node.next_item
    print("None")


# В качестве ответа сдайте только текущую функцию.
# Решение надо отправлять только в виде файла с расширением, которое
# соответствует вашему языку. Иначе даже корректное решение не пройдет тесты.
def solution(node, index):
    def get_node_by_index(node, index):
        while index:
            node = node.next_item
            index -= 1
        return node

    if index == 0:
        node = node.next_item
    else:
        # получаем предыдущий элемент связанного списка
        previous_node = get_node_by_index(node, index - 1)
        # получаем следующий элемент связанного списка
        next_node = get_node_by_index(node, index + 1)
        # заменяем next_item предыдущего элемента на следующий элемент списка
        previous_node.next_item = next_node
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    print_linked_list(new_head)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


if __name__ == '__main__':
    test()
