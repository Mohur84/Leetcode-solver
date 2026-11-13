class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        prefix=[0]
        for ch in s:
            bit=1<<(ord(ch)-ord('a'))
            prefix.append(prefix[-1]^bit)
        result=[]
        for left, right, k in queries:
            mask=prefix[right+1]^prefix[left]
            odd_count=mask.bit_count()
            result.append(odd_count//2<=k)
        return result