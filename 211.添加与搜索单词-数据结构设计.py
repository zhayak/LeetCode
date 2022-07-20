#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True
            

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def helper(self, node, word, start):
        if start == len(word):
            return node.isEnd
        ch = word[start]
        if ch != '.':
            if ch not in node.children:
                return False
            else:
                return self.helper(node.children[ch], word, start + 1)
        else:
            for child in node.children.values():
                if self.helper(child, word, start + 1):
                    return True
            return False
    
    def search(self, word: str) -> bool:
        return self.helper(self.trie, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

