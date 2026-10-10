import heapq
from collections import defaultdict
class Solution:
    def medianSlidingWindow(self, nums, k):
        small = []  # Max-heap using negative values
        large = []  # Min-heap
        delayed = defaultdict(int)
        small_size = 0
        large_size = 0
        result = []
        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed[num] == 0:
                    break
                delayed[num] -= 1
                heapq.heappop(heap)
        def rebalance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune(small)
            elif small_size < large_size:
                heapq.heappush(small, -heapq.heappop(large))
                large_size -= 1
                small_size += 1
                prune(large)
        def add(num):
            nonlocal small_size, large_size
            if not small:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                prune(small)
                if num <= -small[0]:
                    heapq.heappush(small, -num)
                    small_size += 1
                else:
                    heapq.heappush(large, num)
                    large_size += 1
            rebalance()
        def remove(num):
            nonlocal small_size, large_size
            prune(small)
            prune(large)
            delayed[num] += 1
            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1
                if large and num == large[0]:
                    prune(large)
            rebalance()
        def get_median():
            prune(small)
            prune(large)
            if k % 2:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0
        for i, num in enumerate(nums):
            add(num)
            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                result.append(get_median())
        return result