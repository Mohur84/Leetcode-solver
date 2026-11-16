class Node:
    def __init__(self, val, level):
        self.val=val
        self.forward=[None]*(level+1)
class Skiplist:
    MAX_LEVEL=16
    def __init__(self):
        self.head=Node(-1, self.MAX_LEVEL)
        self.level=0
    def random_level(self):
        lvl=0
        while random.random()<0.5 and lvl<self.MAX_LEVEL:
            lvl+=1
        return lvl
    def search(self, target: int) -> bool:
        current=self.head
        for i in range(self.level, -1, -1):
            while(current.forward[i] is not None and current.forward[i].val<target):
                current=current.forward[i]
        current=current.forward[0]
        return current is not None and current.val==target
    def add(self, num: int) -> None:
        update=[None]*(self.MAX_LEVEL+1)
        current=self.head
        for i in range(self.level, -1, -1):
            while(current.forward[i] is not None and current.forward[i].val<num):
                current=current.forward[i]
            update[i]=current
        new_level=self.random_level()
        if new_level>self.level:
            for i in range(self.level+1, new_level+1):
                update[i]=self.head
            self.level=new_level
        new_node=Node(num, new_level)
        for i in range(new_level+1):
            new_node.forward[i]=update[i].forward[i]
            update[i].forward[i]=new_node
    def erase(self, num: int) -> bool:
        update=[None]*(self.MAX_LEVEL+1)
        current=self.head
        for i in range(self.level, -1, -1):
            while(current.forward[i] is not None and current.forward[i].val<num):
                current=current.forward[i]
            update[i]=current
        target=current.forward[0]
        if target is None or target.val!=num:
            return False
        for i in range(self.level+1):
            if update[i].forward[i]==target:
                update[i].forward[i]=target.forward[i]
        while self.level>0 and self.head.forward[self.level] is None:
            self.level-=1
        return True