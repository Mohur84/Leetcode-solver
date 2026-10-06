class Solution:
    def lengthLongestPath(self, input):
        stack=[0]
        answer=0
        for line in input.split('\n'):
            depth=line.count('\t')
            name=line.lstrip('\t')
            while len(stack)>depth+1:
                stack.pop()
            current_length=stack[-1]+len(name)+1
            if '.' in name:
                answer=max(answer, current_length-1)
            else:
                stack.append(current_length)
        return answer