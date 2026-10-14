class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        n=len(nums)
        visited=[False]*n
        max_length=0
        for i in range(n):
            if not visited[i]:
                length=0
                j=i
                while not visited[j]:
                    visited[j]=True
                    length+=1
                    j=nums[j]
                max_length=max(max_length, length)
        return max_length