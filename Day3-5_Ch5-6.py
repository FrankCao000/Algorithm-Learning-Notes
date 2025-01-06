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

# Based on Array
class ArrayQueue:
    def __init__(self, size: int):
        self._nums: list[int] = [0] * size
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._nums)
    
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def push(self, num: int):
        if self._size == self.capacity():
            raise IndexError("Array is full")
        rear: int = (self._front + self._size) % self.capacity()
        self._nums[rear] = num
        self._size += 1

    def pop(self) -> int:
        num: int = self.peek()
        self._front = (self._front + 1) % self.capacity()
        self._size -= 1
        return num
    
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Empty array")
        return self._nums[self._front]
    
    def to_list(self) -> list[int]:
        res = [0] * self.size()
        j: int = self._front
        for i in range(self.size()):
            res[i] = self._nums[(j % self.capacity())]
            j += 1
        return res
    
# Deque
# Based on LinkedList
class ListNode:
    def __init__(self, val: int):
        self.val: int = val
        self.next: ListNode | None = None
        self.prev: ListNode | None = None

class LinkedListDeque:
    def __init__(self):
        self._front: ListNode | None = None
        self._rear: ListNode | None = None
        self._size: int = 0

    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def push(self, num: int, is_front: bool):
        node = ListNode(num)
        if self.is_empty():
            self._front = self._rear = node
        elif is_front:
            self._front.prev = node
            node.next = self._front
            self._front = node
        else:
            self._rear.next = node
            node.prev = self._rear
            self._rear = node
        self._size += 1

    def push_first(self, num: int):
        self.push(num, True)

    def push_last(self, num: int):
        self.push(num, False)

    def pop(self, is_front: bool) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty")
        if is_front:
            val: int = self._front.val
            fnext: ListNode | None = self._front.next
            if fnext != None:
                fnext.prev = None
                self._front.next = None
            self._front = fnext
        else:
            val: int = self._rear.val
            rprev: ListNode | None = self._rear.prev
            if rprev != None:
                rprev.next = None
                self._rear.prev = None
            self._rear = rprev
        self._size -= 1
        return val
    
    def pop_first(self) -> int:
        return self.pop(True)
    
    def pop_last(self) -> int:
        return self.pop(False)
    
    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._front.val
    
    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._rear.val
    
    def to_array(self) -> list[int]:
        node = self._front
        res = [0] * self.size()
        for i in range(self.size()):
            res[i] = node.val
            node = node.next
        return res
    
# Based on Array
class ArrayDeque:
    def __init__(self, capacity: int):
        self._nums: list[int] = [0] * capacity
        self._front: int = 0
        self._size: int = 0

    def capacity(self) -> int:
        return len(self._nums)
    
    def size(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def index(self, i: int) -> int:
        return (i + self.capacity()) % self.capacity()
    
    def push_first(self, num: int):
        if self._size == self.capacity():
            print("Deque is full")
            return
        self._front = self.index(self._front - 1)
        self._nums[self._front] = num

    def push_last(self, num: int):
        if self._size == self.capacity():
            print("Deque is full")
            return
        rear = self.index(self._front + self._size)
        self._nums[rear] = num
        self._size += 1

    def pop_first(self) -> int:
        num = self.peek_first()
        self._front = self.index(self._front - 1)
        self._size -= 1
        return num
    
    def pop_last(self) -> int:
        num = self.peek_last()
        self._size -= 1
        return num
    
    def peek_first(self) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self._nums[self._front]
    
    def peek_last(self) -> int:
        if self.is_empty():
            raise IndexError("Deque is empty")
        last = self.index(self._front + self._size - 1)
        return self._nums[last]
    
    def to_array(self) -> list[int]:
        res = []
        for i in range(self._size):
            res.append(self._nums[self.index(self._front + i)])
        return res

# Array_Hash_Map
class Pair:
    def __init__(self, key: int, val: str):
        self.key = key
        self.val = val
    
class ArrayHashMap:
    def __init__(self):
        self.buckets: list[Pair | None] = [None] * 100

    def hash_func(self, key: int) -> int:
        index = key % 100
        return index
    
    def get(self, key: int) -> str:
        index: int = self.hash_func(key)
        pair: Pair = self.buckets[index]
        if pair is None:
            return None
        return pair.val
    
    def put(self, key: int, val: str):
        pair = Pair(key, val)
        index: int = self.hash_func(key)
        self.buckets[index] = pair

    def remove(self, key: int):
        index: int = self.hash_func(key)
        self.buckets[index] = None

    def entry_set(self) -> list[Pair]:
        result: list[Pair] = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result
    
    def key_set(self) -> list[int]:
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.key)
        return result
    
    def value_set(self) -> list[str]:
        result = []
        for pair in self.buckets:
            if pair is not None:
                result.append(pair.val)
        return result
    
    def print(self):
        for pair in self.buckets:
            if pair is not None:
                print(pair.key, "->", pair.val)

# Hash_Map_Chaining
class HashMapChaining:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets = [[] for _ in range(self.capacity)]

    def hash_func(self, key: int) -> int:
        return key % self.capacity
    
    def get(self, key: int) -> str | None:
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                return pair.val
        return None
    
    def put(self, key: int, val: str):
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val = val
                return
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self,key: int):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break

    def extend(self):
        buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + "->" + pair.val)
            print(res)

# HashMapOpenAddressing
class HashMapOpenAddressing:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0
        self.extend_ratio = 2
        self.buckets: list[Pair | None] = [None] * self.capacity
        self.TOMBSTONE = Pair(-1, "-1")

    def hash_function(self, key: int) -> int:
        return key % self.capacity
    
    def load_factor(self) -> float:
        return self.size / self.capacity
    
    def find_bucket(self, key: int) -> int:
        index = self.hash_function(key)
        firsr_tombstone = -1
        while self.buckets[index] is not None:
            if self.buckets[index].key == key:
                if firsr_tombstone != -1:
                    self.buckets[firsr_tombstone] = self.buckets[index]
                    self.buckets[index] = self.TOMBSTONE
                    return firsr_tombstone
                return index
            if firsr_tombstone == -1 and self.buckets[index] is self.TOMBSTONE:
                firsr_tombstone = index
            index = (index + 1) % self.capacity
        return key if firsr_tombstone == -1 else firsr_tombstone
    
    def get(self, key: int) -> int:
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            return self.buckets[index].val
        return None
    
    def put(self, key: int, val: str):
        if self.load_factor() > self.load_thres:
            self.extend()
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index].val = val
            return
        self.buckets[index] = Pair(key, val)
        self.size += 1

    def remove(self, key: int):
        index = self.find_bucket(key)
        if self.buckets[index] not in [None, self.TOMBSTONE]:
            self.buckets[index] = self.TOMBSTONE
            self.size -= 1
    
    def extend(self):
        buckets_tmp = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [None] * self.capacity
        self.size = 0
        for pair in buckets_tmp:
            if pair not in [None, self.TOMBSTONE]:
                self.put(pair.key, pair.val)
    
    def print(self):
        for pair in self.buckets:
            if pair is None:
                print("None")
            elif pair is self.TOMBSTONE:
                print("TOMBSTONE")
            else:
                print(pair.key, "->", pair.val)

# Simple Hash
def add_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key:
        hash += ord(c)
    return hash % modulus

def mul_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = 31 * hash + ord(c)
    return hash % modulus

def xor_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key:
        hash ^= ord(c)
    return hash % modulus

def rot_hash(key: str) -> int:
    hash = 0
    modulus = 1000000007
    for c in key:
        hash = (hash << 4) ^ (hash >> 28) ^ ord(c)
    return hash % modulus
