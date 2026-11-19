class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups={}
        result=[]
        for person, size in enumerate(groupSizes):
            if size not in groups:
                groups[size]=[]
            groups[size].append(person)
            if len(groups[size])==size:
                result.append(groups[size])
                groups[size]=[]
        return result