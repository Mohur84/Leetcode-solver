class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:
        heap=[]
        current_max=float('-inf')
        for i, arr in enumerate(nums):
            heapq.heappush(heap, (arr[0], i, 0))
            current_max=max(current_max, arr[0])
        best_start=heap[0][0]
        best_end=current_max
        while True:
            current_min, list_idx, elem_idx=heapq.heappop(heap)
            if (current_max-current_min<best_end-best_start or
                (current_max-current_min==best_end-best_start
                and current_min<best_start)):
                best_start=current_min
                best_end=current_max
            next_idx=elem_idx+1
            if next_idx==len(nums[list_idx]):
                break
            next_val=nums[list_idx][next_idx]
            heapq.heappush(heap, (next_val, list_idx, next_idx))
            current_max=max(current_max, next_val)
        return[best_start, best_end]