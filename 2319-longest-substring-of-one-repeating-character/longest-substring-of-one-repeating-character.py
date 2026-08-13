from sortedcontainers import SortedList
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        s = list(s)
        n = len(s)
        brk = SortedList([0, n])
        for i in range(1, n):
            if s[i] != s[i - 1]:
                brk.add(i)
        seg = SortedList()
        for i in range(len(brk) - 1):
            seg.add(brk[i + 1] - brk[i])
        def remove_break(pos):
            i = brk.index(pos)
            left, right = brk[i - 1], brk[i + 1]
            seg.remove(pos - left)
            seg.remove(right - pos)
            seg.add(right - left)
            brk.remove(pos)
        def add_break(pos):
            i = brk.bisect_left(pos)
            left, right = brk[i - 1], brk[i]
            seg.remove(right - left)
            seg.add(pos - left)
            seg.add(right - pos)
            brk.add(pos)
        res = []
        for idx, c in zip(queryIndices, queryCharacters):
            if s[idx] != c:
                s[idx] = c
                for pos in (idx, idx + 1):
                    if 0 < pos < n:
                        need = s[pos] != s[pos - 1]
                        have = pos in brk
                        if need and not have:
                            add_break(pos)
                        elif not need and have:
                            remove_break(pos)
            res.append(seg[-1])
        return res