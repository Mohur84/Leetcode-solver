class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        freq=defaultdict(int)
        for a in nums:
            for b in nums:
                freq[a&b]+=1
        ans=0
        for c in nums:
            for value, count in freq.items():
                if(value&c)==0:
                    ans+=count
        return ans