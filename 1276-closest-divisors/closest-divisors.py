class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        def find_pair(target):
            a=int(target**0.5)
            while target%a!=0:
                a-=1
            b=target//a
            return[b, a]
        pair1=find_pair(num+1)
        pair2=find_pair(num+2)
        if abs(pair1[0]-pair1[1])<abs(pair2[0]-pair2[1]):
            return pair1
        return pair2