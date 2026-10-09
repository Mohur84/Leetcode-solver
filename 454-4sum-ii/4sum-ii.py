class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sums=Counter(
            a+b
            for a in nums1
            for b in nums2
        )
        result=0
        for c in nums3:
            for d in nums4:
                result+=sums[-(c+d)]
        return result