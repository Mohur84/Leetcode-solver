class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        freq=defaultdict(int)
        freq[0]=1
        odd_count=0
        result=0
        for num in nums:
            if num%2==1:
                odd_count+=1
            result+=freq[odd_count-k]
            freq[odd_count]+=1
        return result