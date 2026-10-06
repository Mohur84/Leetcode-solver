class Solution:
    def longestSubstring(self, s, k):
        def solve(left, right):
            if right-left<k:
                return 0
            count=Counter(s[left:right])
            for i in range(left, right):
                if count[s[i]]<k:
                    j=i+1
                    while j<right and count[s[j]]<k:
                        j+=1
                    return max(
                        solve(left, i),
                        solve(j, right)
                    )
            return right-left
        return solve(0, len(s))