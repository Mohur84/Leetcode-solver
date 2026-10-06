class Solution:
    def findNthDigit(self, n):
        digit=1
        count=9
        start=1
        while n>digit*count:
            n-=digit*count
            digit+=1
            count*=10
            start*=10
        number=start+(n-1)//digit
        index=(n-1)%digit
        return int(str(number)[index])