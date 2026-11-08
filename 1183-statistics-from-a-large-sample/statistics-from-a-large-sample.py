class Solution:
    def sampleStats(self, count):
        total = sum(count)
        minimum = -1
        maximum = -1
        mode = 0
        mode_count = 0
        weighted_sum = 0
        for i, freq in enumerate(count):
            if freq > 0:
                if minimum == -1:
                    minimum = i
                maximum = i
                weighted_sum += i * freq
                if freq > mode_count:
                    mode_count = freq
                    mode = i
        mean = weighted_sum / total
        mid1 = (total - 1) // 2
        mid2 = total // 2
        cumulative = 0
        median1 = median2 = 0
        for i, freq in enumerate(count):
            cumulative += freq
            if cumulative > mid1 and median1 == 0:
                median1 = i
            if cumulative > mid2:
                median2 = i
                break
        median = (median1 + median2) / 2
        return [float(minimum), float(maximum), float(mean),
                float(median), float(mode)]