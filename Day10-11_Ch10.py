# Binary_Search
def binary_search(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            return m
    return -1

# Binary_Search_Insertion
def binary_search_insertion_simple(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            return m
    return i

def binary_search_insertion(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1
    return i

# Binary_Search_Edge
def binary_search_left_edge(nums: list[int], target: int) -> int:
    i = binary_search_insertion(nums, target)
    if i == len(nums) or nums[i] != target:
        return -1
    return i