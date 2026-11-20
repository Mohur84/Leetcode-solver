class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        for num in candidates:
            count = arr.count(num)
            if count > n // 4:
                return num
        return -1