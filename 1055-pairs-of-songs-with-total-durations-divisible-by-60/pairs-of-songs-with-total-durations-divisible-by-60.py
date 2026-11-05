class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        count=[0]*60
        result=0
        for t in time:
            remainder=t%60
            complement=(60-remainder)%60
            result+=count[complement]
            count[remainder]+=1
        return result