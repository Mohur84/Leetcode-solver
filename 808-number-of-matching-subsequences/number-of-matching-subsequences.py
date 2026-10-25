class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        positions=defaultdict(list)
        for i, ch in enumerate(s):
            positions[ch].append(i)
        count=0
        for word in words:
            prev=-1
            matched=True
            for ch in word:
                indices=positions[ch]
                j=bisect_right(indices, prev)
                if j==len(indices):
                    matched=False
                    break
                prev=indices[j]
            if matched:
                count+=1
        return count