class Solution:
    def addToArrayForm(self, num, k):
        i = len(num) - 1
        while i >= 0 and k > 0:
            k += num[i]
            num[i] = k % 10
            k //= 10
            i -= 1
        while k > 0:
            num.insert(0, k % 10)
            k //= 10
        return num