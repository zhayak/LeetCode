#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
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
    
    def find_prefix(self, word):
        node = self
        for i in range(len(word)):
            ch = word[i]
            if ch not in node.children:
                return word
            node = node.children[ch]
            if node.isEnd:
                return word[:(i + 1)]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        ans = []
        for prefix in dictionary:
            trie.insert(prefix)
        for word in sentence.split(' '):
            ans.append(trie.find_prefix(word))
        return ' '.join(ans)

# @lc code=end

