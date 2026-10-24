class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:
        n=len(row)
        position=[0]*n
        for i, person in enumerate(row):
            position[person]=i
        swaps=0
        for i in range(0, n, 2):
            person=row[i]
            partner=person^1
            if row[i+1]==partner:
                continue
            partner_pos=position[partner]
            other_partner=row[i+1]
            row[i+1], row[partner_pos]=(
                row[partner_pos],
                row[i+1]
            )
            position[partner]=i+1
            position[other_partner]=partner_pos
            swaps+=1
        return swaps