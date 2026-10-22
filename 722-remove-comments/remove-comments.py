class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        result=[]
        current=[]
        in_block=False
        for line in source:
            i=0
            while i<len(line):
                if in_block:
                    if line[i:i+2]=="*/":
                        in_block=False
                        i+=2
                    else:
                        i+=1
                else:
                    if line[i:i+2]=="//":
                        break
                    elif line[i:i+2]=="/*":
                        in_block=True
                        i+=2
                    else:
                        current.append(line[i])
                        i+=1
            if not in_block and current:
                result.append("".join(current))
                current=[]
        return result