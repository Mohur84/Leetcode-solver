class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","").upper()
        if not s:
            return ""
        first=len(s)%k
        result=[]
        if first:
            result.append(s[:first])
        for i in range(first, len(s), k):
            result.append(s[i:i+k])
        return "-".join(result)