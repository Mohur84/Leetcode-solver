class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        MOD=10**9+7
        dp=[
            [0]*(rollMax[j]+1)
            for j in range(6)
        ]
        for j in range(6):
            dp[j][1]=1
        for _ in range(2, n+1):
            new_dp=[
                [0]*(rollMax[j]+1)
                for j in range(6)
            ]
            for j in range(6):
                for k in range(1, rollMax[j]+1):
                    ways=dp[j][k]
                    if ways==0:
                        continue
                    if k+1<=rollMax[j]:
                        new_dp[j][k+1]=(
                            new_dp[j][k+1]+ways
                        )%MOD
                    for other in range(6):
                        if other!=j:
                            new_dp[other][1]=(
                                new_dp[other][1]+ways
                            )%MOD
            dp=new_dp
        return sum(
            sum(face) for face in dp
        )%MOD