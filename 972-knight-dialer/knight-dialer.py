class Solution:
    def knightDialer(self, n: int) -> int:
        MOD=10**9+7
        moves={
            0:[4, 6],
            1:[6, 8],
            2:[7, 9],
            3:[4, 8],
            4:[0, 3, 9],
            5:[],
            6:[0, 1, 7],
            7:[2, 6],
            8:[1, 3],
            9:[2, 4]
        }
        dp=[1]*10
        for _ in range(n-1):
            new_dp=[0]*10
            for digit in range(10):
                for next_digit in moves[digit]:
                    new_dp[next_digit]+=dp[digit]
                    new_dp[next_digit]%=MOD
            dp=new_dp
        return sum(dp)%MOD