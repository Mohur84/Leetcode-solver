class Solution:
    def smallestPalindrome(self, s):
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        
        half = []
        mid = ""
        for i in range(26):
            half.append(chr(ord('a') + i) * (cnt[i] // 2))
            if cnt[i] % 2 == 1:
                mid = chr(ord('a') + i)
        
        half_str = "".join(half)
        return half_str + mid + half_str[::-1]

sol = Solution()
print(sol.smallestPalindrome("babab"))
print(sol.smallestPalindrome("daccad"))
print(sol.smallestPalindrome("z"))