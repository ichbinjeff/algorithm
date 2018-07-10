import collections

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.lookup = {}
        self.freq_map = collections.defaultdict(collections.OrderedDict)
        self.min_freq = 0
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lookup:
            return -1
        
        freq = self.lookup[key][1]
        self.freq_map[freq].pop(key)
        self.lookup[key][1] = freq+1
        self.freq_map[freq+1][key] = True
        if len(self.freq_map[self.min_freq]) == 0:
            self.min_freq += 1

        return self.lookup[key][0]
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key) != -1:
            self.lookup[key][0] = value
            return 

        if self.capacity == 0:
            return
            
        if len(self.lookup) == self.capacity:
            self.remove_least_freq()

        node = [value, 1]
        self.lookup[key] = node
        self.freq_map[1][key] = True
        self.min_freq = 1

    def remove_least_freq(self):
        min_entry = self.freq_map[self.min_freq].popitem(False)
        del self.lookup[min_entry[0]]
        if len(self.freq_map[self.min_freq]) == 0:
            self.min_freq += 1

lfu = LFUCache(2)
lfu.put(1,1)
lfu.put(2,2)
print lfu.lookup
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)