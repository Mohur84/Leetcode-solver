class Solution:
    def longestWPI(self, hours: list[int]) -> int:
        prefix_sum=0
        seen={}
        result=0
        for i, hour in enumerate(hours):
            if hour>8:
                prefix_sum+=1
            else:
                prefix_sum-=1
            if prefix_sum>0:
                result=i+1
            elif prefix_sum-1 in seen:
                result=max(result, i-seen[prefix_sum-1])
            if prefix_sum not in seen:
                seen[prefix_sum]=i
        return result