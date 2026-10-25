class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq=Counter(s)
        result=[]
        for ch in order:
            result.append(ch*freq[ch])
            freq[ch]=0
        for ch, count in freq.items():
            result.append(ch*count)
        return "".join(result)