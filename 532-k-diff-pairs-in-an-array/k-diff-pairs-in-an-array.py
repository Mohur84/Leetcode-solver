class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        freq=Counter(nums)
        if k==0:
            return sum(count>=2 for count in freq.values())
        return sum(num+k in freq for num in freq)