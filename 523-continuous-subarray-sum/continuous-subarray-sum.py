class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_index={0: -1}
        prefix_sum=0
        for i, num in enumerate(nums):
            prefix_sum+=num
            if k!=0:
                remainder=prefix_sum%k
            else:
                remainder=prefix_sum
            if remainder in remainder_index:
                if i-remainder_index[remainder]>=2:
                    return True
            else:
                remainder_index[remainder]=i
        return False