class Solution:
    def getHint(self, secret, guess):
        bulls=0
        secret_count=[0]*10
        guess_count=[0]*10
        for s, g in zip(secret, guess):
            if s==g:
                bulls+=1
            else:
                secret_count[int(s)]+=1
                guess_count[int(g)]+=1
        cows=0
        for digit in range(10):
            cows+=min(secret_count[digit], guess_count[digit])
        return str(bulls)+"A"+str(cows)+"B"