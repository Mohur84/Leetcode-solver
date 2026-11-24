class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strength=[]
        for i, row in enumerate(mat):
            soldiers=sum(row)
            strength.append((soldiers, i))
        strength.sort()
        return [strength[i][1] for i in range(k)]