class Solution:
    def isSelfCrossing(self, distance):
        n=len(distance)
        for i in range(3, n):
            if distance[i]>=distance[i-2] and \
               distance[i-1]<=distance[i-3]:
               return True
            if i>=4 and \
               distance[i-1]==distance[i-3] and \
               distance[i]+distance[i-4]>=distance[i-2]:
               return True
            if i>=5 and \
               distance[i-2]>=distance[i-4] and \
               distance[i-1]<=distance[i-3] and \
               distance[i-1]+distance[i-5]>=distance[i-3] and \
               distance[i]+distance[i-4]>=distance[i-2]:
               return True
        return False