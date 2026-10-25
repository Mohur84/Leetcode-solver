class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp=[0.0]*(query_row+2)
        dp[0]=float(poured)
        for row in range(query_row):
            next_row=[0.0]*(query_row+2)
            for col in range(row+1):
                overflow=max(0.0, dp[col]-1.0)/2.0
                next_row[col]+=overflow
                next_row[col+1]+=overflow
            dp=next_row
        return min(1.0, dp[query_glass])