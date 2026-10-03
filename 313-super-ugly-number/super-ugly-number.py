class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly=[1]
        k=len(primes)
        pointers=[0]*k
        for _ in range(1, n):
            next_num=min(
                primes[i]*ugly[pointers[i]]
                for i in range(k)
            )
            ugly.append(next_num)
            for i in range(k):
                if primes[i]*ugly[pointers[i]]==next_num:
                    pointers[i]+=1
        return ugly[-1]