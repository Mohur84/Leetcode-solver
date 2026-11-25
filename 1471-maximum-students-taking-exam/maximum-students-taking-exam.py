class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        valid_masks = []
        for row in seats:
            available = 0
            for j in range(n):
                if row[j] == '.':
                    available |= (1 << j)
            masks = []
            for mask in range(1 << n):
                if mask & ~available:
                    continue
                if mask & (mask << 1):
                    continue
                masks.append(mask)
            valid_masks.append(masks)
        dp = {0: 0}
        for masks in valid_masks:
            new_dp = {}
            for curr in masks:
                count = bin(curr).count('1')
                for prev, value in dp.items():
                    if (prev & (curr << 1)) == 0 and \
                       (prev & (curr >> 1)) == 0:
                        new_dp[curr] = max(
                            new_dp.get(curr, 0),
                            value + count
                        )
            dp = new_dp
        return max(dp.values())