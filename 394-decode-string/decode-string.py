class Solution:
    def decodeString(self, s):
        counts=[]
        strings=[]
        current=""
        number=0
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            elif ch=='[':
                counts.append(number)
                strings.append(current)
                number=0
                current=""
            elif ch==']':
                repeat=counts.pop()
                previous=strings.pop()
                current=previous+current*repeat
            else:
                current+=ch
        return current