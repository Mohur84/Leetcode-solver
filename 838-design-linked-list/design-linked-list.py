class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class MyLinkedList:
    def __init__(self):
        self.head=Node()
        self.size=0
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        current=self.head.next
        for _ in range(index):
            current=current.next
        return current.val
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0:
            index=0
        if index>self.size:
            return
        previous=self.head
        for _ in range(index):
            previous=previous.next
        new_node=Node(val, previous.next)
        previous.next=new_node
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        previous=self.head
        for _ in range(index):
            previous=previous.next
        previous.next=previous.next.next
        self.size-=1