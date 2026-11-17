from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        count = Counter(s)
        if all(count[ch] == target for ch in "QWER"):
            return 0
        left = 0
        result = n
        for right in range(n):
            count[s[right]] -= 1
            while all(count[ch] <= target for ch in "QWER"):
                result = min(result, right - left + 1)
                count[s[left]] += 1
                left += 1
        return result