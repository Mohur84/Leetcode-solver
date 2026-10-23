class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start="0"*(n-1)
        seen=set()
        result=[]
        def dfs(node:str)->None:
            for digit in range(k):
                edge=node+str(digit)
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    result.append(str(digit))
        dfs(start)
        return start + "".join(reversed(result))