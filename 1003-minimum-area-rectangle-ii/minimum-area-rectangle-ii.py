from collections import defaultdict
from math import sqrt
class Solution:
    def minAreaFreeRect(self, points):
        n = len(points)
        diagonals = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                mx = x1 + x2
                my = y1 + y2
                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                diagonals[(mx, my, dist)].append((i, j))
        min_area = float('inf')
        for pairs in diagonals.values():
            for i in range(len(pairs)):
                for j in range(i + 1, len(pairs)):
                    a, b = pairs[i]
                    c, d = pairs[j]
                    x1 = points[a][0] - points[c][0]
                    y1 = points[a][1] - points[c][1]
                    x2 = points[a][0] - points[d][0]
                    y2 = points[a][1] - points[d][1]
                    area = abs(x1 * y2 - y1 * x2)
                    min_area = min(min_area, area)
        return 0.0 if min_area == float('inf') else float(min_area)