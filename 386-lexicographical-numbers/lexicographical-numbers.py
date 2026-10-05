class Solution:
    def lexicalOrder(self, n):
        result=[]
        def dfs(num):
            if num>n:
                return
            result.append(num)
            for digit in range(10):
                next_num=num*10+digit
                if next_num>n:
                    break
                dfs(next_num)
        for i in range(1, 10):
            dfs(i)
        return result