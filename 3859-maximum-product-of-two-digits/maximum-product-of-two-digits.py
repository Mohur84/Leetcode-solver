class Solution:
    def maxProduct(self, n):
        a = 0
        b = 0
        while n:
            d = n % 10
            n = n // 10
            if d > a:
                b = a
                a = d
            elif d > b:
                b = d
        return a * b