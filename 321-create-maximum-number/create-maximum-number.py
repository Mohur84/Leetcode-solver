class Solution:
    def maxNumber(self, nums1, nums2, k):
        def max_subsequence(nums, length):
            drop = len(nums) - length
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
        def greater(a, i, b, j):
            while i < len(a) and j < len(b) and a[i] == b[j]:
                i += 1
                j += 1
            if i == len(a):
                return False
            if j == len(b):
                return True
            return a[i] > b[j]
        def merge(a, b):
            result = []
            i = j = 0
            while i < len(a) or j < len(b):
                if i == len(a):
                    result.append(b[j])
                    j += 1
                elif j == len(b):
                    result.append(a[i])
                    i += 1
                elif greater(a, i, b, j):
                    result.append(a[i])
                    i += 1
                else:
                    result.append(b[j])
                    j += 1
            return result
        best = []
        start = max(0, k - len(nums2))
        end = min(k, len(nums1))
        for x in range(start, end + 1):
            a = max_subsequence(nums1, x)
            b = max_subsequence(nums2, k - x)
            candidate = merge(a, b)
            if candidate > best:
                best = candidate
        return best