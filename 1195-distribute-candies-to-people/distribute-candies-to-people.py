class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        result=[0]*num_people
        give=1
        person=0
        while candies>0:
            amount=min(give, candies)
            result[person]+=amount
            candies-=amount
            give+=1
            person=(person+1)%num_people
        return result