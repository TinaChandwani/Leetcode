class LFUCache:
    '''
    Using Ordered Dict
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_map = {}
        self.cache = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v,f = self.cache[key]
        del self.freq_map[f][key]
        if f == self.min_freq and not self.freq_map[f]:
            self.min_freq += 1
        f = f + 1
        self.cache[key] = (v, f)
        if f not in self.freq_map:
            self.freq_map[f] = OrderedDict()
        self.freq_map[f][key] = None
        self.freq_map[f].move_to_end(key,last=False)
        return v
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity == len(self.cache):
                evict_key, _ = self.freq_map[self.min_freq].popitem(last=True)
                del self.cache[evict_key]
            freq = 1
            if freq not in self.freq_map:
                self.freq_map[freq] = OrderedDict()
            self.freq_map[freq][key] = None
            self.freq_map[freq].move_to_end(key,last=False) # Always Pushes in front
            self.min_freq = 1
            self.cache[key] = (value,freq)

        else:
            v,f = self.cache[key]
            self.cache[key] = (value, f)
            g = self.get(key)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)