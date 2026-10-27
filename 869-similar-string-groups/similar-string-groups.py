class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        n=len(strs)
        def similar(a:str, b:str)->bool:
            differences=0
            for x, y in zip(a, b):
                if x!=y:
                    differences+=1
                    if differences>2:
                        return False
            return differences==0 or differences==2
        visited=[False]*n
        groups=0
        for i in range(n):
            if visited[i]:
                continue
            groups+=1
            stack=[i]
            visited[i]=True
            while stack:
                current=stack.pop()
                for j in range(n):
                    if not visited[j] and similar(strs[current], strs[j]):
                        visited[j]=True
                        stack.append(j)
        return groups