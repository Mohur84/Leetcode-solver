class Solution:
    def restoreIpAddresses(self, s):
        ans=[]
        def backtrack(index, parts):
            if len(parts)==4:
                if index==len(s):
                    ans.append(".".join(parts))
                return
            for length in range(1, 4):
                if index + length > len(s):
                    break
                part=s[index:index+length]
                if(part.startswith("0") and len(part)>1) or int(part)>255:
                    continue
                parts.append(part)
                backtrack(index+length, parts)
                parts.pop()
        backtrack(0, [])
        return ans