from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        mid = ""
        half = [0] * 26
        total = 0

        for c in sorted(cnt):
            if cnt[c] % 2:
                mid = c
            x = cnt[c] // 2
            half[ord(c) - ord('a')] = x
            total += x

        # Total number of distinct half permutations
        perms = 1
        rem = total
        for f in half:
            if f:
                perms *= comb(rem, f)
                rem -= f

        if perms < k:
            return ""

        ans = []

        while total:
            rem = total - 1

            for i in range(26):
                if half[i] == 0:
                    continue

                # Number of permutations if this character is chosen
                ways = perms * half[i] // total

                if ways >= k:
                    ans.append(chr(i + ord('a')))
                    perms = ways
                    half[i] -= 1
                    total -= 1
                    break
                else:
                    k -= ways

        left = "".join(ans)
        return left + mid + left[::-1]