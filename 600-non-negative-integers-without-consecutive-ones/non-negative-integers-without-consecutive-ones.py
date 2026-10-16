class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [0] * 32
        dp[0] = 1
        dp[1] = 2
        for i in range(2, 32):
            dp[i] = dp[i - 1] + dp[i - 2]
        bits = bin(n)[2:]
        result = 0
        prev_bit = 0
        length = len(bits)
        for i, bit in enumerate(bits):
            if bit == '1':
                result += dp[length - i - 1]
                if prev_bit == 1:
                    return result
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1