class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:
        MOD=10**9+7
        def kadane(nums):
            current=0
            best=0
            for num in nums:
                current=max(0, current+num)
                best=max(best, current)
            return best
        total=sum(arr)
        if k==1:
            return kadane(arr)%MOD
        best_two=kadane(arr+arr)
        if total>0:
            answer=best_two+(k-2)*total
        else:
            answer=best_two
        return answer%MOD