class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        count=[0]*121
        for age in ages:
            count[age]+=1
        prefix=[0]*121
        for age in range(1, 121):
            prefix[age]=prefix[age-1]+count[age]
        requests=0
        for age in range(15, 121):
            if count[age]==0:
                continue
            min_age=age//2+8
            eligible=prefix[age]-prefix[min_age-1]
            requests+=count[age]*(eligible-1)
        return requests