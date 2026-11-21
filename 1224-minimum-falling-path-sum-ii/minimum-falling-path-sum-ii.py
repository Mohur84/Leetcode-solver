class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        first_min, second_min, first_idx = 0, 0, -1
        for row in grid:
            curr_first, curr_second, curr_idx = float('inf'), float('inf'), -1
            for j, val in enumerate(row):
                curr_sum = val + (first_min if j != first_idx else second_min)
                if curr_sum < curr_first:
                    curr_second = curr_first
                    curr_first = curr_sum
                    curr_idx = j
                elif curr_sum < curr_second:
                    curr_second = curr_sum
            first_min, second_min, first_idx = curr_first, curr_second, curr_idx
        return first_min