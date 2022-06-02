
class Node:

    def __init__(self, value, nextNode=None):
        self.val = value
        self.next = nextNode

class Bucket:

    def __init__(self):
        self.head = Node(0)
        
    def exists(self, val):
        cur = self.head.next
        while cur:
            if cur.val == val:
                return True
            cur = cur.next
        return False

    def insert(self, val):
        if not self.exists(val):
            node = Node(val, self.head.next)
            self.head.next = node

    def delete(self, val):
        pre = self.head
        cur = self.head.next
        while cur:
            if cur.val == val:
                pre.next = cur.next
                return 
            pre = cur
            cur = cur.next

class MyHashSet:

    def __init__(self):
        self.m = 1009
        self.bucket = [Bucket() for i in range(self.m)]

    def _hash(self, key):
        return key % self.m   

    def add(self, key: int) -> None:
        self.bucket[self._hash(key)].insert(key)        

    def remove(self, key: int) -> None:
        self.bucket[self._hash(key)].delete(key)   

    def contains(self, key: int) -> bool:
        """
        return true if this set contains the specified element
        """
        return self.bucket[self._hash(key)].exists(key)  


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)