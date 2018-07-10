class ListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = ListNode("#", 0)
        self.tail = ListNode("#", 0)
        self.lookup = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lookup:
            return None
        node = self.lookup[key]
        self.delete_node(node)
        self.move_to_head(node)
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = None
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value   
            self.delete_node(node)
        else:
            if len(self.lookup) == self.capacity:
                del self.lookup[self.tail.prev.key]
                self.delete_node(self.tail.prev)
            node = ListNode(key, value)

            self.lookup[key] = node

        self.move_to_head(node)

        
    def delete_node(self, node):
        print "node val: {0}, pre: {1}, next:{2}".format(node.val, node.prev, node.next)
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None

    def move_to_head(self, node):
        next = self.head.next
        self.head.next = node
        next.prev = node
        node.prev = self.head
        node.next = next

s = LRUCache(1)
s.put(2,1)
print s.get(2)
print s.lookup
s.put(3,2)
print s.get(2)
print s.get(3)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)