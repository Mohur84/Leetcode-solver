class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        count_s=Counter(s)
        count_t=Counter(t)
        steps=0
        for ch in count_s:
            if count_s[ch]>count_t[ch]:
                steps+=count_s[ch]-count_t[ch]
        return steps