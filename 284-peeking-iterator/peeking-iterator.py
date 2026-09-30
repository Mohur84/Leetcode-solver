class PeekingIterator:
    def __init__(self, iterator):
        self.iterator=iterator
        self.next_value=iterator.next() if iterator.hasNext() else None
    def peek(self):
        return self.next_value
    def next(self):
        current=self.next_value
        if self.iterator.hasNext():
            self.next_value=self.iterator.next()
        else:
            self.next_value=None
        return current
    def hasNext(self):
        return self.next_value is not None