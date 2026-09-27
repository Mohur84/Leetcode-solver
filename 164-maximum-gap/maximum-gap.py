class Solution:
    def maximumGap(self, nums):
        n=len(nums)
        if n<2:
            return 0
        minVal=min(nums)
        maxVal=max(nums)
        if minVal==maxVal:
            return 0
        bucketSize=max(1,(maxVal-minVal)//(n-1))
        bucketCount=(maxVal-minVal)//bucketSize+1
        buckets=[[float("inf"), float("-inf")]for _ in range(bucketCount)]
        for num in nums:
            idx=(num-minVal)//bucketSize
            buckets[idx][0]=min(buckets[idx][0], num)
            buckets[idx][1]=max(buckets[idx][1], num)
        maxGap=0
        prevMax=minVal
        for bucketMin, bucketMax in buckets:
            if bucketMin==float("inf"):
                continue
            maxGap=max(maxGap, bucketMin-prevMax)
            prevMax=bucketMax
        return maxGap