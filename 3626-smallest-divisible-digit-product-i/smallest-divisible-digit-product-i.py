class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            p = 1
            x = i
            while x:
                p *= x % 10
                x //= 10
            if p % t == 0:
                return i
            i += 1