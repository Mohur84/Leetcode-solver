class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        states=minutesToTest//minutesToDie+1
        pigs=0
        capacity=1
        while capacity<buckets:
            capacity*=states
            pigs+=1
        return pigs