class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            count = 0
            divisor_sum = 0
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    count += 1
                    divisor_sum += i
                    if i != num // i:
                        count += 1
                        divisor_sum += num // i
                    if count > 4:
                        break
            if count == 4:
                total += divisor_sum
        return total