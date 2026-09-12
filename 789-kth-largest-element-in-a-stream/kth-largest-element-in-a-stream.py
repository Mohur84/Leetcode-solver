import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k=k
        self.minHeap=[]
        for num in nums:
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap)>k:
                heapq.heappop(self.minHeap)
    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap)>self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
