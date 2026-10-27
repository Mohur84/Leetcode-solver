class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        result=[]
        MAX_INT=2**31-1
        n=len(num)
        def backtrack(index:int)->bool:
            if index==n:
                return len(result)>=3
            value=0
            for i in range(index, n):
                if i>index and num[index]=='0':
                    break
                value=value*10+int(num[i])
                if value>MAX_INT:
                    break
                if len(result)>=2:
                    expected=result[-1]+result[-2]
                    if value<expected:
                        continue
                    if value>expected:
                        break
                result.append(value)
                if backtrack(i+1):
                    return True
                result.pop()
            return False
        backtrack(0)
        return result