def for_loop(n: int) -> int:
    res = 0
    for i in range (1,n+1):
        res += 1
    return res

def while_loop(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res

def while_loop_ii(n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res

def nested_for_loop(n: int) -> str:
    res = ""
    for i in range(1, n+1):
        for j in range(1, n+1):
            res += f"({i}, {j}), "
    return res

def recur(n: int) -> int:
    if n == 1:
        return 1
    res = recur(n-1)
    return n + res

def tail_recur(n, res):
    if n == 0:
        return
    return tail_recur(n-1, res +n)

def fib(n: int) -> int:
    if n == 1 or n ==2:
        return n - 1
    res = fib(n-1) + fib(n-2)
    return res

def for_loop_recur(n: int) -> int:
    stack = []
    res = 0
    for i in range(n, 0, -1):
        stack.append(i)
    while stack:
        res += stack.pop()
    return res

def algo_A(n : int):
    print(0)

def algo_B(n: int):
    for _ in range(n):
        print(0)

def algo_C(n : int):
    for _ in range(10000):
        print(0)

##Time-Complexity
##O(1)
def constant(n: int) -> int:
    count = 0
    size = 10000
    for _ in range(size):
        count += 1
    return count

##O(n)
def linear(n: int) -> int:
    count = 0
    for _ in range(n):
        count += 1
    return count

def array_traversal(nums: list[int]) -> int:
    count = 0
    for num in nums:
        count += 1
    return count

##O(n^2)
def quadratic(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

##O((n-1)n/2) -> O(n^2)
def bubble_sort(nums: list[int]) -> int:
    count = 0
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                tmp: int = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
                count += 3
    return count

##O(2^n)
def exponnential(n: int) -> int:
    count = 0
    base = 1
    for _ in range(n):
        for _ in range(base):
            count += 1
        base += 2
    # count = 1 + 2 + 4 + 8 + ... + 2^(n-1) = 2^n - 1
    return count

def exp_recur(n: int) -> int:
    if n == 1:
        return 1
    return exp_recur(n-1) + exp_recur(n-1) + 1

## Olog(n)
def logarithmic(n: int) -> int:
    count = 0
    while n > 1:
        n = n/2
        count += 1
    return count

def log_recur(n: int) -> int:
    if n <= 1:
        return 0
    return log_recur(n/2) + 1

## O(nlog(n))
def linear_log_recur(n: int) -> int:
    if n <= 1:
        return 1
    count = linear_log_recur(n//2) + linear_log_recur(n//2)
    for _ in range(n):
        count += 1
    return count

## O(n!)
def factorial_recur(n: int) -> int:
    if n == 0:
        return 1
    count = 0
    for _ in range(n):
        count += factorial_recur(n-1)
    return count

## Best/Worst time complexity
import random
def random_numbers(n: int) -> list[int]:
    nums = [i for i in range(1, n + 1)]
    random.shuffle(nums)
    return nums

def find_one(nums: list[int]) -> int:
    for i in range(len(nums)):
    ## when 1 is in the front: best time complexity O(1)
    ## when i is in the end: worst time complexity O(n)
        if nums[i] == 1:
            return i
    return -1

##Space-Complexity
## O(1)
def function() -> int:
    return 0

from modules import ListNode
def constant(n: int):
    a = 0
    nums = [0] * 1000
    node = ListNode(0)
    ## variable in loop takes space_complexity of O(1)
    for _ in range(n):
        c = 0
    ## function in loop takes space_complexity of O(1)
    for _ in range(n):
        function()

## O(n)
def linear(n: int):
    nums = [0] * n
    hmap = dict[int, str]()
    for i in range(n):
        hmap[i] = str(i)

def linear_recur(n: int):
    print("Recursed n = ", n)
    if n == 1:
        return
    linear_recur(n - 1)

## O(n^2)
def quadratic(n: int):
    num_matrix = [[0] * n for _ in range(n)]

## O(n(n+1)/2) -> O(n^2)
def quadratic_recur(n: int) -> int:
    if n <= 0:
        return 0
    nums = [0] * n
    return quadratic_recur(n - 1)

## O(2^n)
from modules import TreeNode
def build_tree(n: int) -> TreeNode | None:
    if n == 0:
        return None
    root = TreeNode(0)
    root.left = build_tree(n - 1)
    root.right = build_tree(n -1)
    return root
    
