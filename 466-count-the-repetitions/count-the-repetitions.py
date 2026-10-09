class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0
        if not set(s2).issubset(set(s1)):
            return 0
        index = 0
        count_s2 = 0
        count_s1 = 0
        seen = {}
        while count_s1 < n1:
            if index in seen:
                prev_s1, prev_s2 = seen[index]
                cycle_s1 = count_s1 - prev_s1
                cycle_s2 = count_s2 - prev_s2
                remaining = n1 - count_s1
                cycles = remaining // cycle_s1
                count_s1 += cycles * cycle_s1
                count_s2 += cycles * cycle_s2
                if count_s1 == n1:
                    break
            else:
                seen[index] = (count_s1, count_s2)
            for char in s1:
                if char == s2[index]:
                    index += 1
                    if index == len(s2):
                        index = 0
                        count_s2 += 1
            count_s1 += 1
        return count_s2 // n2