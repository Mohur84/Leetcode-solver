class Solution:
    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        temp = [0] * (n + 1)
        count = 0
        size = 1
        while size <= n:
            left = 0
            while left <= n - size:
                mid = left + size
                right = min(left + 2 * size, n + 1)
                lo = mid
                hi = mid
                for i in range(left, mid):
                    while lo < right and prefix[lo] - prefix[i] < lower:
                        lo += 1
                    while hi < right and prefix[hi] - prefix[i] <= upper:
                        hi += 1
                    count += hi - lo
                i = left
                j = mid
                k = left
                while i < mid and j < right:
                    if prefix[i] <= prefix[j]:
                        temp[k] = prefix[i]
                        i += 1
                    else:
                        temp[k] = prefix[j]
                        j += 1
                    k += 1
                while i < mid:
                    temp[k] = prefix[i]
                    i += 1
                    k += 1
                while j < right:
                    temp[k] = prefix[j]
                    j += 1
                    k += 1
                for i in range(left, right):
                    prefix[i] = temp[i]
                left += 2 * size
            size *= 2
        return count