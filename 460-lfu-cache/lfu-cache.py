class LFUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.values={}
        self.freq={}
        self.groups=defaultdict(OrderedDict)
        self.min_frq=0
    def _update(self, key):
        f=self.freq[key]
        del self.groups[f][key]
        if not self.groups[f]:
            del self.groups[f]
            if self.min_freq==f:
                self.min_freq+=1
        self.freq[key]=f+1
        self.groups[f+1][key]=None
    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self._update(key)
        return self.values[key]
    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return
        if key in self.values:
            self.values[key]=value
            self._update(key)
            return
        if len(self.values)>=self.capacity:
            key_to_remove,_=self.groups[self.min_freq].popitem(last=False)
            del self.values[key_to_remove]
            del self.freq[key_to_remove]
        self.values[key]=value
        self.freq[key]=1
        self.groups[1][key]=None
        self.min_freq=1