class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        count=defaultdict(int)
        freq=defaultdict(int)
        max_freq=0
        result=0
        for i, num in enumerate(nums):
            old_freq=count[num]
            if old_freq>0:
                freq[old_freq]-=1
            count[num]+=1
            new_freq=count[num]
            freq[new_freq]+=1
            max_freq=max(max_freq, new_freq)
            n=i+1
            if max_freq==1:
                result=n
            elif freq[1]==1 and freq[max_freq]*max_freq+1==n:
                result=n
            elif freq[max_freq]==1 and freq[max_freq-1]*(max_freq-1)+max_freq==n:
                result=n
        return result