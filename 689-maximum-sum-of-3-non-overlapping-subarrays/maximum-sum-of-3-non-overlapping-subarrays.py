class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        window_count=n-k+1
        window_sum=[0]*window_count
        current_sum=sum(nums[:k])
        window_sum[0]=current_sum
        for i in range(1, window_count):
            current_sum+=nums[i+k-1]-nums[i-1]
            window_sum[i]=current_sum
        left=[0]*window_count
        best=0
        for i in range(window_count):
            if window_sum[i]>window_sum[best]:
                best=i
            left[i]=best
        right=[0]*window_count
        best=window_count-1
        for i in range(window_count-1, -1, -1):
            if window_sum[i]>=window_sum[best]:
                best=i
            right[i]=best
        answer=[-1, -1, -1]
        max_total=-1
        for mid in range(k, window_count-k):
            first=left[mid-k]
            third=right[mid+k]
            total=(
                window_sum[first]
                +window_sum[mid]
                +window_sum[third]
            )
            if total>max_total:
                max_total=total
                answer=[first, mid, third]
        return answer