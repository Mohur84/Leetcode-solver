class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count=defaultdict(int)
        first={}
        last={}
        for i, num in enumerate(nums):
            count[num]+=1
            if num not in first:
                first[num]=i
            last[num]=i
        degree=max(count.values())
        result=len(nums)
        for num in count:
            if count[num]==degree:
                length=last[num]-first[num]+1
                result=min(result, length)
        return result