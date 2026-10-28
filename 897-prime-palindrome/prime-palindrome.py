class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            if x % 3 == 0:
                return x == 3
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True
        if 8 <= n <= 11:
            return 11
        length = len(str(n))
        while True:
            if length % 2 == 0:
                length += 1
                continue
            start = 10 ** (length // 2)
            end = 10 ** (length // 2 + 1)
            for half in range(start, end):
                s = str(half)
                palindrome = int(s + s[-2::-1])
                if palindrome >= n and is_prime(palindrome):
                    return palindrome
            length += 2