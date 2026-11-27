class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        max_flipped=0
        ans=0
        for i, num in enumerate(flips):
            max_flipped=max(max_flipped, num)
            if max_flipped==i+1:
                ans+=1
        return ans