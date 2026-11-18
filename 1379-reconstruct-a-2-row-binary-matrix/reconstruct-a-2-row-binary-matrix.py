class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []
        row1 = [0] * len(colsum)
        row2 = [0] * len(colsum)
        for i, x in enumerate(colsum):
            if x == 2:
                row1[i] = 1
                row2[i] = 1
                upper -= 1
                lower -= 1
        if upper < 0 or lower < 0:
            return []
        for i, x in enumerate(colsum):
            if x == 1:
                if upper > 0:
                    row1[i] = 1
                    upper -= 1
                elif lower > 0:
                    row2[i] = 1
                    lower -= 1
                else:
                    return []
        if upper == 0 and lower == 0:
            return [row1, row2]
        return []