class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        n = len(words)
        while i < n:
            j = i
            line_length = 0
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1
            gaps = j - i - 1
            line = ""
            if j == n or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - line_length
                even = total_spaces // gaps
                extra = total_spaces % gaps
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (even + (1 if k - i < extra else 0))
                line += words[j - 1]
            res.append(line)
            i = j
        return res
