class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1==s2:
            return 0
        queue=deque([(s1, 0)])
        visited={s1}
        n=len(s1)
        while queue:
            current, swaps=queue.popleft()
            i=0
            while current[i]==s2[i]:
                i+=1
            for j in range(i+1, n):
                if current[j]==s2[i] and current[j]!=s2[j]:
                    chars=list(current)
                    chars[i], chars[j]=chars[j], chars[i]
                    nxt=''.join(chars)
                    if nxt==s2:
                        return swaps+1
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, swaps+1))
        return -1