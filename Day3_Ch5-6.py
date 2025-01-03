# Stack
from modules import ListNode
# Based on Linked List
class LinkedListStack:
    def __init__(self):
        self._peek: ListNode | None = None
        self._size: int = 0
    
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def push(self, val: int):
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self._peek.val
    
    def to_list(self) -> list[int]:
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr
    
# Based on Array
class ArrayStack:
    def __init__(self):
        self._stack: list[int] = []

    def size(self) -> int:
        return len(self._stack)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def push(self, item: int):
        self._stack.append(item)

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self._stack.pop()
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Empty stack")
        return self._stack[-1]
    
    def to_list(self) -> list[int]:
        return self._stack
    
# Queue
# Based on Linked List
class LinkedListQueue:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size
    
    def  is_empty(self) -> bool:
        return self._size == 0
    
    def push(self, num: int):
        node = ListNode(num)
        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def pop(self) -> int:
        num = self.peek()
        self._front = self._front.next
        self._szie -= 1
        return num
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Empty queue")
        return self._front.val
    
    def to_list(self) -> list[int]:
        queue = []
        temp = self._front
        while temp:
            queue.append(temp.val)
            temp = temp.next
        return queue

    
