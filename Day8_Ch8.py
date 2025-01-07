# Heap
# Max Heap
import heapq
class MaxHeap:
    def __init__(self, nums: list[int]):
        self.max_heap = nums
        for i in range(self.parent(self.size() - 1), -1, -1):
            self.sift_down(i)
        
    def left(self, i: int) -> int:
        return 2 * i + 1

    def right(self, i: int) -> int:
        return 2 * i + 2

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def peek(self) -> int:
        return self.max_heap[0]

    def push(self, val: int):
        self.max_heap.append(val)
        self.sift_up(self.size() - 1)

    def sift_up(self, i: int):
        while True:
            p = self.parent(i)
            if p < 0 or self.max_heap[i] <= self.max_heap[p]:
                break
            self.swap(i,p)
            i = p

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Empty heap")
        self.swap(0, self.size - 1)
        val = self.max_heap.pop()
        self.sift_down(0)
        return val
    
    def sift_down(self, i: int):
        while True:
            l, r, ma = self.left(i), self.right(i), i
            if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
                ma = l
            if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
                ma = r
            if ma == i:
                break
            self.swap(i, ma)
            i = ma

#top_k
    def top_k_heap(nums: list[int], k: int) -> list[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapop(heap)
                heapq.heappush(heap, nums[i])
        return heap
