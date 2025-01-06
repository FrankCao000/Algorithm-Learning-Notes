# List
import random
def random_access(nums: list[int]):
    random_index = random.randint(0, len(nums) - 1)
    random_num = nums[random_index]
    return random_num

# A flawed verison of insert function, 
# as it will delete the element in the end of the array.
def insert(nums: list[int], num: int, index: int):
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i - 1]
    num[index] = num

def remove(nums: list[int], index: int):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

def traverse(nums: list[int]):
    count = 0
    for i in range(len(nums)):
        count += nums[i]
    for num in nums:
        count += num
    for i, num in enumerate(nums):
        count += nums[i]
        count += num

def find(nums: list[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def extend(nums: list[int], enlarge: int) -> list[int]:
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res

# Linked-List
from modules import ListNode
def insert(n0: ListNode, P: ListNode):
    n1 = n0.next
    P.next = n1
    n0.next = P

def remove(n0: ListNode):
    if not n0.next:
        return
    # n0 -> P -> n1
    P = n0.next
    n1 = P.next
    n0.next = n1   

def access(head: ListNode, index: int) -> ListNode | None:
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head: ListNode, target: int) -> int:
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1

# MyList
class MyList:
    def __init__(self):
        self._capacity: int = 10
        self._arr: list[int] = [0] * self._capacity
        self._size: int = 0
        self._extend_ratio: int = 2
    
    def size(self) -> int:
        return self._size
    
    def capacity(self) -> int:
        return self._capacity
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("Over the bound")
        return self._arr[index]
    
    def set(self, num: int, index: int):
        if index < 0 or index >= self._sze:
            raise IndexError("Over the bound")
        self._arr[index] = num

    def add(self, num: int):
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("Over the bound")
        if self._size == self._capacity():
            self.extend_capacity()
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
        self._size += 1

    def remove(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("Over the bound")
        num = self._arr[index]
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
        self._size -= 1
        return num
    
    def extend_capacity(self):
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        return self._arr[: self._size]
