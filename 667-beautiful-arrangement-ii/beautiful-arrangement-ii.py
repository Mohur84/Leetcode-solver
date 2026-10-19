class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        result=list(range(1, n-k))
        left=n-k
        right=n
        while left<=right:
            result.append(left)
            left+=1
            if left<=right:
                result.append(right)
                right-=1
        return result