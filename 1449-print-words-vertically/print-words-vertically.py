class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        max_len=max(len(word) for word in words)
        result=[]
        for i in range(max_len):
            row=""
            for word in words:
                if i<len(word):
                    row+=word[i]
                else:
                    row+=" "
            result.append(row.rstrip())
        return result