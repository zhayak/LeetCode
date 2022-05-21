#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def __init__(self):
        self.data = []
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = ""
        if root is None:
            return '#;'
        ans += str(root.val) + ';'
        ans += self.serialize(root.left)
        ans += self.serialize(root.right)
        return ans
    
    def helper(self):
        val = self.data[0]
        self.data = self.data[1:]
        if val == '#':
            return None
        root = TreeNode(int(val))
        root.left = self.helper()
        root.right = self.helper()
        return root
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data.split(';')
        return self.helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

