class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count=0
            for ch in string:
                if ch=='(':
                    count+=1
                elif ch==')':
                    count-=1
                    if count<0:
                        return False
            return count==0
        result=[]
        queue={s}
        found=False
        while queue:
            next_level=set()
            for string in queue:
                if is_valid(string):
                    result.append(string)
                    found=True
            if found:
                return result
            for string in queue:
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue
                    new_string=string[:i]+string[i+1:]
                    next_level.add(new_string)
            queue=next_level
        return [""]