class Solution:
    def isValid(self, code: str) -> bool:
        stack=[]
        i=0
        n=len(code)
        while i<n:
            if i>0 and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False
                j=code.find("]]>", i+9)
                if j==-1:
                    return False
                i=j+3
            elif code.startswith("</", i):
                j=code.find(">", i+2)
                if j==-1:
                    return False
                tag=code[i+2:j]
                if not stack or stack[-1]!=tag:
                    return False
                stack.pop()
                i=j+1
            elif code.startswith("<", i):
                j=code.find(">", i+1)
                if j==-1:
                    return False
                tag=code[i+1:j]
                if not (1<=len(tag)<=9):
                    return False
                if not all('A'<=c<='Z' for c in tag):
                    return False
                stack.append(tag)
                i=j+1
            else:
                if not stack:
                    return False
                i+=1
        return not stack and n>0