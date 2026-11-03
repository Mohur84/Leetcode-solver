class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        prefix_sum = 0
        result = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in remainder_count:
                result += remainder_count[remainder]
            remainder_count[remainder] = (
                remainder_count.get(remainder, 0) + 1
            )
        return result