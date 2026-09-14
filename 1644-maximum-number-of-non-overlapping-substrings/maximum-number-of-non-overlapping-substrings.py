class Solution:
    def maxNumOfSubstrings(self, s):
        first = [len(s)] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i
        intervals = []
        for c in range(26):
            if last[c] == -1:
                continue
            l, r = first[c], last[c]
            i = l
            valid = True
            while i <= r:
                idx = ord(s[i]) - ord('a')
                if first[idx] < l:
                    valid = False
                    break
                r = max(r, last[idx])
                i += 1
            if valid:
                intervals.append((l, r))
        intervals.sort(key=lambda x: x[1])
        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r
        return ans