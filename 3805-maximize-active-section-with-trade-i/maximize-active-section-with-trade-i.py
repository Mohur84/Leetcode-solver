class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        t = '1' + s + '1'
        n = len(t)
        
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j
        
        ones_count = s.count('1')
        best_gain = 0
        
        for k in range(1, len(runs) - 1):
            ch, length = runs[k]
            if ch == '1':
                left_ch, left_len = runs[k - 1]
                right_ch, right_len = runs[k + 1]
                if left_ch == '0' and right_ch == '0':
                    best_gain = max(best_gain, left_len + right_len)
        
        return ones_count + best_gain