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