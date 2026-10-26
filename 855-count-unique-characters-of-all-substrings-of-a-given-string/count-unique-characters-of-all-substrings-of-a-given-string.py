class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n=len(s)
        positions={}
        for i, ch in enumerate(s):
            if ch not in positions:
                positions[ch]=[-1]
            positions[ch].append(i)
        total=0
        for ch, indices in positions.items():
            indices.append(n)
            for j in range(1, len(indices)-1):
                prev=indices[j-1]
                curr=indices[j]
                nxt=indices[j+1]
                total+=(curr-prev)*(nxt-curr)
        return total