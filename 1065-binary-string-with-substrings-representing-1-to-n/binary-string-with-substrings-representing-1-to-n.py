class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n+1):
            binary=bin(i)[2:]
            if binary not in s:
                return False
        return True