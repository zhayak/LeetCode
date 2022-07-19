#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def addLast(self, x):
        x.prev = self.tail.prev
        x.next = self.tail
        self.tail.prev.next = x
        self.tail.prev = x
        self.size += 1
    
    def removeFirst(self):
        if self.size == 0:
            return
        first = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.size -= 1
        return first
    
    def removeNode(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        self.size -= 1


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = DoubleList()
        self.capacity = capacity
        self.mapping = {}

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        x = self.mapping[key]
        self.cache.removeNode(x)
        self.cache.addLast(x)
        return x.value

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.cache.removeNode(self.mapping[key])
            del self.mapping[key]
            x = Node(key, value)
            self.cache.addLast(x)
            self.mapping[key] = x
        else:
            if self.cache.size == self.capacity:
                node = self.cache.removeFirst()
                del self.mapping[node.key]
            x = Node(key, value)
            self.cache.addLast(x)
            self.mapping[key] = x


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

