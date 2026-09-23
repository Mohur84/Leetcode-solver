class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(i)
        heights.pop()
        return maxArea
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        ans = 0
        for row in matrix:
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))
        return ans