class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n=len(arr)
        heap=[]
        for i in range(n-1):
            heapq.heappush(
                heap, (arr[i]/arr[n-1], i, n-1)
            )
        for _ in range(k):
            _, i, j=heapq.heappop(heap)
            if j-1>i:
                heapq.heappush(
                    heap, (arr[i]/arr[j-1], i, j-1)
                )
        return[arr[i], arr[j]]