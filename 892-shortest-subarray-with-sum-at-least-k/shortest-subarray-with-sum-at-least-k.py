class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        dq=deque()
        shortest=n+1
        for i in range(n+1):
            while dq and prefix[i]-prefix[dq[0]]>=k:
                shortest=min(shortest, i-dq.popleft())
            while dq and prefix[dq[-1]]>=prefix[i]:
                dq.pop()
            dq.append(i)
        return shortest if shortest<=n else -1