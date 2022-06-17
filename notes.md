# 链表
注意：一般链表题都会先创建一个dummy node，最后返回dummy.next，这样可以有效避免空指针问题。

## [21.合并两个有序链表.py](21.合并两个有序链表.py)
Create a dummy node to append to. Create a pointer to move along the result list.<br>
dummy = ListNode(0)<br>
p = dummy<br>
...<br>
p = p.next<br>
...<br>
return dummy.next<br>

## [23.合并k个升序链表.py](23.合并k个升序链表.py)
### Method 1
Define a function to merge two sorted lists (same as 21), then merge two by two<br>
(Note: use binary method to merge two by two)
### Method 2
**[TODO]** Use priority queue to get the mininum of the k elements

## [19.删除链表的倒数第-n-个结点.py](19.删除链表的倒数第-n-个结点.py)
使用两个指针通过一次遍历找到倒数第n+1个节点（快指针先走n+1步，然后同时移动快慢指针直到快指针为空），然后删除第n个节点即可。

## [876.链表的中间结点.py](876.链表的中间结点.py)
使用快慢两个指针，快指针一次走两步，慢指针一次走一步

## [141.环形链表.py](141.环形链表.py)
同样使用快慢两个指针，若两指针相遇，则有环；若快指针为空，则无环

## [142.环形链表-ii.py](142.环形链表-ii.py)
假设slow走了k步，则fast一定比slow多走了k步，这多走的k步其实就是fast在环里转圈，所以k的值一定是环长度的整数倍。<br>
假设相遇点距环的起点的距离为m，则环的起点距head的距离为k-m，也就是说从 head前进 k-m 步即可到达环起点。同时，如果从相遇点继续前进 k-m 步，也恰好到达环起点。

## [160.相交链表.py](160.相交链表.py)
我们可以让p1遍历完链表A之后开始遍历链表B，让p2遍历完链表B之后开始遍历链表A，这样相当于逻辑上两条链表接在了一起。如果这样进行拼接，就可以让p1和p2同时到达相交节点c1。<br>
即使没有相交节点，也会同时到达空节点。

## [206.反转链表.py](206.反转链表.py)
### 方法一：普通翻转
```
class Solution:
    def reverserList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            post = head.next
            head.next = prev
            prev = head
            head = post
        return prev
```
### 方法二：递归
```
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
```

## [92.反转链表-ii.py](92.反转链表-ii.py)
### 方法一
找到左侧节点，左侧前一节点，右侧节点，右侧后一节点；然后将右侧节点的next设为None，再将之前所有节点翻转（直接使用206的代码翻转），然后拼接。
### 方法二：递归
https://labuladong.github.io/algo/2/17/17/

## [25.k-个一组翻转链表.py](25.k-个一组翻转链表.py)
先写一个函数用来翻转节点a到节点b之间的链表，再用递归的方法逐一翻转并将翻转后的链表连接即可。<br>
https://labuladong.github.io/algo/2/17/18/

## [234.回文链表.py](234.回文链表.py)
### 方法一
先用快慢指针找到链表的中点，然后将后半段链表翻转，再进行比较
### 方法二
**[TODO]** 利用链表后序遍历(https://labuladong.github.io/algo/2/17/19/)

<br><br>

# 数组
## [26.删除有序数组中的重复项.py](26.删除有序数组中的重复项.py)
遍历数组的同时用一个指针记录当前无重复数组的index，如果遍历到的数和当前指针所指的数不同，则将当前指针向前移动一格，并将该位置的数字替换

## [83.删除排序链表中的重复元素.py](83.删除排序链表中的重复元素.py)
与上一题思路一致，但注意结束后断开与后续重复节点的连接。slow.next = None

## [27.移除元素.py](27.移除元素.py)
## [283.移动零.py](283.移动零.py)
与26题思路一致

## [167.两数之和-ii-输入有序数组.py](167.两数之和-ii-输入有序数组.py)
## [344.反转字符串.py](344.反转字符串.py)
左右两指针，从两侧到中间靠拢

## [5.最长回文子串.py](5.最长回文子串.py)
遍历字符串，以每个字符为中心，使用左右两指针向两侧扩展找到最长回文串。需要注意的是，回文串可以是奇数也可以是偶数个，所以每个中心要考虑到这两种情况。

## [303.区域和检索-数组不可变.py](303.区域和检索-数组不可变.py)
使用前缀和的方法，不用反复进行累加计算，只需在初始化时计算一次即可

## [304.二维区域和检索-矩阵不可变.py](304.二维区域和检索-矩阵不可变.py)
使用二维数组前缀和，注意计算公式

## [1109.航班预订统计.py](1109.航班预订统计.py) 
## [1094.拼车.py](1094.拼车.py)
使用差分数组的方法，构造diff数组，对diff数组进行操作，最后recover最终数组。<br>
**差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减**

## [48.旋转图像.py](48.旋转图像.py)
矩阵顺时针旋转90度，相当于先按对角线镜面翻转，再把每一行的元素翻转

## [54.螺旋矩阵.py](54.螺旋矩阵.py)
## [59.螺旋矩阵-ii.py](59.螺旋矩阵-ii.py)
采用上下左右四个边界来控制for循环
```
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        upper, lower, left, right = 0, m-1, 0, n-1
        res = []
        while len(res) < m * n:
            if upper <= lower:
                for j in range(left, right+1):
                    res.append(matrix[upper][j])
                upper += 1
            if left <= right:
                for i in range(upper, lower+1):
                    res.append(matrix[i][right])
                right -= 1
            if upper <= lower:
                for j in range(right, left-1, -1):
                    res.append(matrix[lower][j])
                lower -= 1
            if left <= right:
                for i in range(lower, upper-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
```

## [76.最小覆盖子串.py](76.最小覆盖子串.py)
滑动窗口算法

## [567.字符串的排列.py](567.字符串的排列.py)
## [438.找到字符串中所有字母异位词.py](438.找到字符串中所有字母异位词.py)
滑动窗口算法，注意左指针收缩的条件为字符串长度不超过s1的长度
## [3.无重复字符的最长子串.py](3.无重复字符的最长子串.py)
滑动窗口算法，注意左侧窗口收缩的条件

## [704.二分查找.py](704.二分查找.py)
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
```

## [34.在排序数组中查找元素的第一个和最后一个位置.py](34.在排序数组中查找元素的第一个和最后一个位置.py)
查找左边界和右边界时，循环条件 `while left + 1 < right` 防止越界，循环结束时分别检验`left`和`right`的值来决定使用哪个

## [528.按权重随机选择.py](528.按权重随机选择.py)
将权重转换为presum的数组，随机生成一个整数后在presum数组中进行二分搜索找到对应的下标返回

## [875.爱吃香蕉的珂珂.py](875.爱吃香蕉的珂珂.py)
我们可以知道吃香蕉速度的下限（1）和上限（最大那堆的个数），只需要在这个整数区间内逐一尝试即可找到满足条件的最小速度。并且我们知道，吃香蕉所需时间为吃香蕉速度的单调函数。因此使用二分搜索即可

## [1011.在-d-天内送达包裹的能力.py](1011.在-d-天内送达包裹的能力.py)
原理同875，构建函数使用二分搜索

## [410.分割数组的最大值.py](410.分割数组的最大值.py)
原理同875，尝试搜索符合条件的最小的sum值，所以构建一个函数，给定m个分割和一个target sum，来判断是否可行，根据是否可行来决定缩小左边界还是右边界

## [870.优势洗牌.py](870.优势洗牌.py)
将两个数组按照从达到小排序，逐一进行比较，如果可以胜出，则直接选取这个数；如果不能胜出，则选用最小的数。注意在排序前记录一下排序前后对应的index，以便最后将答案map回最初的顺序

<br><br>

# 单调栈
## 模板：下一个更大元素
https://labuladong.github.io/algo/2/21/60/ <br>
倒序遍历：stack中存储数值
```
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(nums[i])
        return res
```
正序遍历：stack中存储下标
```
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
        return results
```

## [739.每日温度.py](739.每日温度.py)
套用单调栈模板，只不过在stack中存储index

## [503.下一个更大元素-ii.py](503.下一个更大元素-ii.py)
循环数组技巧：直接将数组*2即可

## [316.去除重复字母.py](316.去除重复字母.py)
## [1081.不同字符的最小子序列.py](1081.不同字符的最小子序列.py)
用一个counter来记录字符串中每个字母剩余的次数，用stack来记录最终的结果。遍历字符串，如果该字符已经存在于栈中，则不必再管；若不存在，则比较其和栈顶元素的大小，若栈顶元素比它大，且栈顶元素在之后的字符串中还有，那意味着我们应该放弃当前的栈顶元素，保留之后的栈顶元素，以确保最小字典序。因此，将栈顶元素弹出，将当前字符压入栈中。

<br><br>

# 二叉树
前序位置的代码在刚刚进入一个二叉树节点的时候执行；<br>
后序位置的代码在将要离开一个二叉树节点的时候执行；<br>
中序位置的代码在一个二叉树节点左子树都遍历完，即将开始遍历右子树的时候执行。<br>
前序位置的代码只能从函数参数中获取父节点传递来的数据，而后序位置的代码不仅可以获取参数数据，还可以获取到子树通过函数返回值传递回来的数据<br>

遇到一道二叉树的题目时的通用思考过程是：
1. 是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现
2. 是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值
3. 无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做
```
traverse(TreeNode root) {
    if (root is None)
        return
    // 前序位置
    traverse(root.left);
    // 中序位置
    traverse(root.right);
    // 后序位置
}
```

## [102.二叉树的层序遍历.py](102.二叉树的层序遍历.py)
```
def levelOrderTraverse(self, root):
    if root is None:
        return []

    from collections import deque   
    queue = deque([root])
    result = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

## [104.二叉树的最大深度.py](104.二叉树的最大深度.py)
二叉树后序遍历，返回左子树和右子树的较大的值

## [226.翻转二叉树.py](226.翻转二叉树.py)
基本的后序遍历框架

## [116.填充每个节点的下一个右侧节点指针.py](116.填充每个节点的下一个右侧节点指针.py)
直接用while循环一直root.left循环下去，root.left就是每一层的开始，依次把每一层的节点的next连接起来

## [114.二叉树展开为链表.py](114.二叉树展开为链表.py)
将左右子树分别展开后，将展开后的左子树连接到root.right，再将展开后的右子树连到左子树末端

## [654.最大二叉树.py](654.最大二叉树.py)
找到数组中的最大值构建root节点，再递归调用分别用左右数组构建左右子树即可

## [105.从前序与中序遍历序列构造二叉树.py](105.从前序与中序遍历序列构造二叉树.py)
preorder[0]就是根节点的值，在inorder中找到根节点的值，根节点左侧的为左子树的值，根节点右侧的为右子树的值。通过递归调用分别构建左右子树与根节点连接即可

## [106.从中序与后序遍历序列构造二叉树.py](106.从中序与后序遍历序列构造二叉树.py)
类似于105，postorder[-1]为根节点的值

## [889.根据前序和后序遍历构造二叉树.py](889.根据前序和后序遍历构造二叉树.py)
preorder[0]和postorder[-1]是根节点的值，preorder[1]在postorder中的位置为postorder左子树的截止位置，剩余部分为右子树，递归调用构建即可。注意：给定前序和后序，构建出来的符合条件的树可能不唯一

## [297.二叉树的序列化与反序列化.py](297.二叉树的序列化与反序列化.py)
使用前序遍历进行序列化和反序列化，注意反序列化时的写法。另外由于节点值可能是两位数或者复数，存成字符串时要以分号隔开才行

## [652.寻找重复的子树.py](652.寻找重复的子树.py)
traverse的时候将每一个子树都序列化存到dictionary中，如果发现重复的子树，则将其root加入到res当中

<br><br>

# 二叉搜索树
- 对于 BST 的每一个节点 node，左子树节点的值都比 node 的值要小，右子树节点的值都比 node 的值大
- 对于 BST 的每一个节点 node，它的左侧子树和右侧子树都是 BST

<br><br>

# 数据结构设计
## [380.o-1-时间插入、删除和获取随机元素.py](380.o-1-时间插入、删除和获取随机元素.py)
使用一个 `val_to_index` 的dictionary加上数组来记录数据。删除时，将想要删除的元素与数组末尾的元素进行交换，然后再删除末尾的元素。

## [710.黑名单中的随机数.py](710.黑名单中的随机数.py)
https://labuladong.github.io/algo/2/18/30/
构建一个mapping，将黑名单的数map到不是黑名单的数字上。将所有黑名单的数移到数组末尾，这样只需在数组前半部分随机取数即可。随机取到一个数后，查看其是否在mapping中，如果在，意味着它是黑名单中的数，返回它map到的白名单的数即可。

<br><br>

# 解题思路
### **化繁为简，重复利用**
将比较复杂的题目想办法转化/分解成简单的题目，利用简单题目的代码<br>
例如：92可直接利用206的代码
### **回文**
寻找回文串是从中间向两端扩展，判断回文串是从两端向中间收缩。对于单链表，无法直接倒序遍历，可以造一条新的反转链表，可以利用链表的后序遍历，也可以用栈结构倒序处理单链表
### **二分搜索问题的泛化**
当我们可以通过一个个试出来答案，且试答案的函数为单调函数的时候，可以考虑用泛化二分搜索（参考875）
### **数据结构设计**
如果想高效地，等概率地随机获取元素，就要使用数组作为底层容器，同时配合dictionary来构建index的索引。为了维护数组的连续性，通常使用交换元素的方式，将想要删除的元素交换到数组末尾再pop掉。

<br><br>

# Review List
- [25.k-个一组翻转链表.py](25.k-个一组翻转链表.py)
- [76.最小覆盖子串.py](76.最小覆盖子串.py)
- [567.字符串的排列.py](567.字符串的排列.py)
- [710.黑名单中的随机数.py](710.黑名单中的随机数.py)
- [739.每日温度.py](739.每日温度.py)
- [316.去除重复字母.py](316.去除重复字母.py)
- [543.二叉树的直径.py](543.二叉树的直径.py)
- [116.填充每个节点的下一个右侧节点指针.py](116.填充每个节点的下一个右侧节点指针.py)
- [297.二叉树的序列化与反序列化.py](297.二叉树的序列化与反序列化.py)
- [652.寻找重复的子树.py](652.寻找重复的子树.py)