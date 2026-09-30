class Solution:
    def addOperators(self, num, target):
        result=[]
        def backtrack(index, expression, value, last):
            if index==len(num):
                if value==target:
                    result.append(expression)
                return
            for end in range(index+1, len(num)+1):
                if end>index+1 and num[index]=='0':
                    break
                current_str=num[index:end]
                current=int(current_str)
                if index==0:
                    backtrack(
                        end,
                        current_str,
                        current,
                        current
                    )
                else:
                    backtrack(
                        end,
                        expression+"+"+current_str,
                        value+current,
                        current
                    )
                    backtrack(
                        end,
                        expression+"-"+current_str,
                        value-current,
                        -current
                    )
                    backtrack(
                        end,
                        expression+"*"+current_str,
                        value-last+last*current,
                        last*current
                    )
        backtrack(0, "", 0, 0)
        return result