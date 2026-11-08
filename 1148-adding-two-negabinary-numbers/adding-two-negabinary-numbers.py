class Solution:
    def addNegabinary(self, arr1, arr2):
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry != 0:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            bit = total % 2
            carry = (total - bit) // -2
            result.append(bit)
        result.reverse()
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return result if result else [0]