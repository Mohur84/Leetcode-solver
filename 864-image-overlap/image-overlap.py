class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n=len(img1)
        ones1=[
            (r, c)
            for r in range(n)
            for c in range(n)
            if img1[r][c]==1
        ]
        ones2=[
            (r, c)
            for r in range(n)
            for c in range(n)
            if img2[r][c]==1
        ]
        shifts=Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift=(r1-r2, c1-c2)
                shifts[shift]+=1
        return max(shifts.values(),default=0)