
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0:
            return -1

        curr = self.head
        i = 0

        while curr:
            if i == index:
                return curr.val

            curr = curr.next
            i += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return

        curr = self.head
        i = 0

        # Find the node immediately before the insertion position
        while curr and i < index - 1:
            curr = curr.next
            i += 1

        if not curr:
            return

        new_node = ListNode(val)

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node
        else:
            self.tail = new_node

        curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0:
            return

        curr = self.head
        i = 0

        while curr and i < index:
            curr = curr.next
            i += 1

        if not curr:
            return

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        curr.prev = None
        curr.next = None
