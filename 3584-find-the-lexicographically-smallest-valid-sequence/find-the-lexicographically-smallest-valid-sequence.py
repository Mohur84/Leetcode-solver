class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        match_pos = [-1] * (m + 1)
        match_pos[m] = n  # empty suffix always "matches" from position n
        i = n - 1
        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1
            if i < 0:
                match_pos[j] = -1
            else:
                match_pos[j] = i
                i -= 1
        result = []
        i, j = 0, 0
        used_change = False
        while j < m and i < n:
            if word1[i] == word2[j]:
                result.append(i)
                i += 1
                j += 1
            elif not used_change and match_pos[j + 1] != -1 and i + 1 <= match_pos[j + 1]:
                result.append(i)
                i += 1
                j += 1
                used_change = True
            else:
                i += 1
        return result if j == m else []