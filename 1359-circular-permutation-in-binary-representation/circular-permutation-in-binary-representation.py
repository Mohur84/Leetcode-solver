class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result=[]
        for i in range(1<<n):
            gray=i^(i>>1)
            result.append(gray^start)
        return result