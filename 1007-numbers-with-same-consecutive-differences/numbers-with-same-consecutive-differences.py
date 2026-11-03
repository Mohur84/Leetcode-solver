class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        if n==1:
            return list(range(10))
        result=[]
        def dfs(num, length):
            if length==n:
                result.append(num)
                return
            last=num%10
            next_digits={last+k, last-k}
            for digit in next_digits:
                if 0<=digit<=9:
                    dfs(num*10+digit, length+1)
        for digit in range(1, 10):
            dfs(digit, 1)
        return result