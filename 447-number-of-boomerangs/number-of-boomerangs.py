class Solution:
    def numberOfBoomerangs(self, points):
        result=0
        for i in range(len(points)):
            count=defaultdict(int)
            x1, y1 = points[i]
            for j in range(len(points)):
                if i==j:
                    continue
                x2, y2 = points[j]
                dist=(x1-x2)**2+(y1-y2)**2
                count[dist]+=1
            for k in count.values():
                result+=k*(k-1)
        return result