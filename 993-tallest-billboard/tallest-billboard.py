class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp={0:0}
        for rod in rods:
            new_dp=dp.copy()
            for diff, shorter in dp.items():
                new_diff=diff+rod
                new_dp[new_diff]=max(
                    new_dp.get(new_diff, 0),
                    shorter
                )
                new_diff=abs(diff-rod)
                new_shorter=shorter+min(diff, rod)
                new_dp[new_diff]=max(
                    new_dp.get(new_diff, 0),
                    new_shorter
                )
            dp=new_dp
        return dp[0]