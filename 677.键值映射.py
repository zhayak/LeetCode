#
# @lc app=leetcode.cn id=677 lang=python3
#
# [677] 键值映射
#

# @lc code=start
class Trie:

    def __init__(self):
        self.children = {}
        self.value = 0

    def insert(self, key, val):
        node = self
        for ch in key:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
            node.value += val
    
    def sum(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.value

class MapSum:

    def __init__(self):
        self.root = Trie()
        self.mapping = {}
    
    def insert(self, key: str, val: int) -> None:
        if key not in self.mapping:
            self.mapping[key] = val
            self.root.insert(key, val)
        else:
            self.root.insert(key, val - self.mapping[key])
            self.mapping[key] = val

    def sum(self, prefix: str) -> int:
        return self.root.sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

