class Solution:
    def isAdditiveNumber(self, num):
        n = len(num)
        def add(a, b):
            i = len(a) - 1
            j = len(b) - 1
            carry = 0
            res = []
            while i >= 0 or j >= 0 or carry:
                x = ord(a[i]) - ord('0') if i >= 0 else 0
                y = ord(b[j]) - ord('0') if j >= 0 else 0
                s = x + y + carry
                res.append(chr(ord('0') + s % 10))
                carry = s // 10
                i -= 1
                j -= 1
            return ''.join(reversed(res))
        def dfs(start, a, b):
            if start == n:
                return True
            expected = add(a, b)
            if not num.startswith(expected, start):
                return False
            return dfs(
                start + len(expected),
                b,
                expected
            )
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            a = num[:i]
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break

                b = num[i:j]

                if dfs(j, a, b):
                    return True

        return False