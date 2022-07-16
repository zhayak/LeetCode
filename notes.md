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

## [496.下一个更大元素-i.py](496.下一个更大元素-i.py)
对nums2套用单调栈模板，同时使用一个dictionary记录nums1中元素值与下标的对应关系。如果nums2中的元素存在于nums1中，则将其下一个更大元素记录到答案中

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
## [230.二叉搜索树中第k小的元素.py](230.二叉搜索树中第k小的元素.py)
二叉树前序遍历的结果就是一个升序数组，所以只需进行前序遍历，遍历到第k个元素停止即可

## [538.把二叉搜索树转换为累加树.py](538.把二叉搜索树转换为累加树.py)
## [1038.从二叉搜索树到更大和树.py](1038.从二叉搜索树到更大和树.py)
先遍历右子树，再遍历左子树，即为从大到小排序。将每个节点的值累加并替换即可

## [98.验证二叉搜索树.py](98.验证二叉搜索树.py)
在dfs的时候要carry一个最大值和最小值，与root的值进行比较

## [701.二叉搜索树中的插入操作.py](701.二叉搜索树中的插入操作.py)
插入一个数，就是先找到插入位置，然后进行插入操作。[700.二叉搜索树中的搜索.py](700.二叉搜索树中的搜索.py)为二叉搜索树的查找，只需在该查找框架中稍微改动，插入元素即可。函数要返回TreeNode类型，并且要对递归调用的返回值进行接收

## [450.删除二叉搜索树中的节点.py](450.删除二叉搜索树中的节点.py)
同样套用二叉搜索树查找框架，然后分情况补全细节（见代码注释）

<br><br>

# 图
## [797.所有可能的路径.py](797.所有可能的路径.py)
```
class Solution:
    def dfs(self, graph, curr_node, path, paths):
        if curr_node == len(graph) - 1:
            paths.append(path[:])
            return
        for next_node in graph[curr_node]:
            path.append(next_node)
            self.dfs(graph, next_node, path, paths)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(graph, 0, [0], paths)
        return paths
```

## [207.课程表.py](207.课程表.py)
## [210.课程表-ii.py](210.课程表-ii.py)
拓扑排序：（时间和空间复杂度均为O(V+E)）
1. 建图并记录所有节点的入度
2. 将所有入度为0的节点加入队列。
3. 取出队首的结点，将其加入拓扑序列
4. 访问该结点所有的邻接点nxt，将nxt的入度减1，当减到0后，将nxt加入队列
5. 重复步骤3、4，直到队列为空
6. 如果拓扑序列个数等于节点数，代表该有向图无环，且存在拓扑序。

<br><br>

# 宽度优先搜索BFS
## [111.二叉树的最小深度.py](111.二叉树的最小深度.py)
利用基本的BFS模板即可

## [752.打开转盘锁.py](752.打开转盘锁.py)
BFS，注意特殊情况，就是当“0000”在deadends中时，直接返回-1

## [200.岛屿数量.py](200.岛屿数量.py)
BFS，进行bfs时把每个访问过的陆地加入到visited中，对每个未被加入到visited中的陆地进行bfs并计数。注意bfs时也要把初始的结点加入到visited里面中去

## [1254.统计封闭岛屿的数目.py](1254.统计封闭岛屿的数目.py)
先把位于四条边界上的陆地进行bfs但不计数，再将剩余陆地bfs并计数

## [1020.飞地的数量.py](1020.飞地的数量.py)
类似于上一题，先把位于边界上的陆地进行bfs，再数一下剩余不在visited中的陆地的数量即可

## [695.岛屿的最大面积.py](695.岛屿的最大面积.py)
稍微修改一下bfs，让其返回岛屿的面积，再找出最大的面积即可

## [1905.统计子岛屿.py](1905.统计子岛屿.py)
用bfs遍历grid2中的岛屿，同时在bfs算法中检查grid2中的每一块陆地在grid1中是不是也是陆地，如果都是那么该岛屿一定是一个子岛屿

<br><br>

# 动态规划
## [322.零钱兑换.py](322.零钱兑换.py)
使用一个长度为amount+1的数组dp，dp[i]表示凑成总金额i所需的最少硬币个数，dp[amount]则为所求答案。注意的是dp的值初始化为amount+1，因为如果有解那么硬币个数不可能超过amount，所以如果dp[i]==amount+1意味着无法凑成总金额i

## [300.最长递增子序列.py](300.最长递增子序列.py)
dp[i]表示以nums[i]结尾的数列的最长递增子序列的长度（必须包含nums[i])，返回值为dp中的最大值

## [354.俄罗斯套娃信封问题.py](354.俄罗斯套娃信封问题.py)
将信封按照宽度增序排序，宽度相同时长度递减排序 `envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))`
这样就转变为针对长度的最长递增子序列问题。但直接使用上一题dp的方法会超时（O(N^2)），需要使用二分查找法（O(NlogN)）
https://labuladong.github.io/algo/3/23/67/

## [931.下降路径最小和.py](931.下降路径最小和.py)
dp[i][j]表示下降到(i, j)的最小路径和。
dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j].
因为可以降落到最后一行的任何问题，需要返回min(dp[n-1])

## [72.编辑距离.py](72.编辑距离.py)
dp[i][j]表示word1[:i]到word2[:j]的最小编辑距离。<br>
如果word1[i] == word2[j]，则该位置无需编辑，dp[i][j] = dp[i-1][j-1] <br>
若不等，则有三种情况：<br>
1. 给word1插入一个和word2最后的字母相同的字母, dp[i][j] = dp[i][j-1] + 1
2. 删除word1的最后一个字母，dp[i][j] = dp[i-1][j] + 1
3. 把word1的最后一个字母替换成word2的最后一个字母，dp[i][j] = dp[i-1][j-1] + 1

## [53.最大子数组和.py](53.最大子数组和.py)
dp[i]表示以nums[i]结尾包括nums[i]的最大子数组和，返回值为max(dp)

## [1143.最长公共子序列.py](1143.最长公共子序列.py)
dp[i][j]表示text1[:i]和text2[:j]的最长公共子序列
1. 若text1[i] == text2[j]，dp[i][j] = dp[i-1][j-1] + 1
2. 若不等，dp[i][j] = max(dp[i-1][j], dp[i][j-1])

## [583.两个字符串的删除操作.py](583.两个字符串的删除操作.py)
dp[i][j]表示word1[:i]和word2[:j]所需的最小删除次数
1. 若word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
2. 若不等，dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

## [712.两个字符串的最小ascii删除和.py](712.两个字符串的最小ascii删除和.py)
dp[i][j]表示str1[:i]和str2[:j]的最小删除和
1. 若str1[i] == str2[j], dp[i][j] = dp[i-1][j-1]
2. 若不等，dp[i][j] = min(dp[i-1][j] + ord(s1[i]), dp[i][j-1] + ord(s2[j]))

## [1312.让字符串成为回文串的最少插入次数.py](1312.让字符串成为回文串的最少插入次数.py)
## [516.最长回文子序列.py](516.最长回文子序列.py)
转化为求s和其倒序字符串的最长公共子序列，最少插入次数即为字符串长度减去最长公共子序列的长度，最长回文子序列即为最长公共子序列的长度

## [416.分割等和子集.py](416.分割等和子集.py)
问题可转化为0-1型背包问题，即是否可以找到几个物品放入容量为sum/2的背包使背包正好装满。

## [518.零钱兑换-ii.py](518.零钱兑换-ii.py)
dp[i][j]表示使用前i个硬币凑出总额j的组合数量
```
if coins[i-1] > j:
    dp[i][j] = dp[i-1][j]
else:
    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
```

## [494.目标和.py](494.目标和.py)
可转化为分割子集问题。集合A为加号的数，集合B为减号的数，则sum(A) - sum(B) = target => sum(A) = (target + sum(nums)) / 2<br>
即从nums中选出和为(target+sum(nums))/2的子集<br>
dp[i][j]表示使用前i个数使其和为j<br>
注意这里的base case为dp[0][0] = 1。dp[i][0]不一定为1，比如nums = [0, 0, 0]时，dp[1][0] = 2, dp[2][0] = 4

## [174.地下城游戏.py](174.地下城游戏.py)
反向dp，从右下角向左上角填充。dp[i][j]表示从(i,j)出发走到右下角所需的最小血量。base case为 dp[m-1][n-1] = 1 if dungeon[i][j] > 0 else -dungeon[i][j] + 1
```
dp[i][j] = max(min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j], 1)
```

## [514.自由之路.py](514.自由之路.py)
注意如何使用备忘录记录中间结果，否则会超时

## [787.k-站中转内最便宜的航班.py](787.k-站中转内最便宜的航班.py)
与514有些类似，也需要使用备忘录

## [10.正则表达式匹配.py](10.正则表达式匹配.py)
注意状态转移方程的定义，主要是*要特殊处理
https://leetcode.cn/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/

## [887.鸡蛋掉落.py](887.鸡蛋掉落.py)
将问题返回来想，f(t,k)表示可以做t次操作，而且有k个鸡蛋，那么我们能找到答案的最高的楼层n。如果我们求出了所有的f(t,k)，那么只需要找出最小的满足f(t,k)≥n的t。
```
f[i][1] = i, f[1][j] = 1
f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
```

## [198.打家劫舍.py](198.打家劫舍.py)
dp[i]表示偷前i个房子所能偷到的最大金额。对于第i个房子可以选择偷或者不偷。dp[i] = max(dp[i-1], dp[i-2]+nums[i])

## [213.打家劫舍-ii.py](213.打家劫舍-ii.py)
房子围成一个圈意味着第一个房子和第二个房子不能同时抢。可以把环拆分为两个数列，一个不包含第一个元素，一个不包含最后一个元素。套用上一题的方法分别求出这两种情况的最大值，返回更大的那个即可

## [337.打家劫舍-iii.py](337.打家劫舍-iii.py)
递归调用 + 备忘录

## **买卖股票问题思路模板**
dp[i][k][0]表示第i天最大交易次数为k且没持有股票时的最大收益
```
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
```
dp[i][k][1]表示第i天最大交易次数为k且持有股票时的最大收益
```
dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
```
最后返回dp[n-1][0]即可

## [122.买卖股票的最佳时机-ii.py](122.买卖股票的最佳时机-ii.py)
没有交易次数限制，所以可以去掉k这个维度<br>
dp[i][0]表示若第i天没持有股票的最大收益，dp[i][1]表示若第i天持有股票的最大收益
```
dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
```

## [309.最佳买卖股票时机含冷冻期.py](309.最佳买卖股票时机含冷冻期.py)
稍作变形即可，需要注意一下i=1时特殊情况的处理：dp[i][1] = max(dp[i - 1][1], -prices[i])

## [714.买卖股票的最佳时机含手续费.py](714.买卖股票的最佳时机含手续费.py)
和122基本一样，只需要把手续费加入到买入价格里即可（加到卖出价格里也可以）

## [123.买卖股票的最佳时机-iii.py](123.买卖股票的最佳时机-iii.py)
## [188.买卖股票的最佳时机-iv.py](188.买卖股票的最佳时机-iv.py)
直接套用买卖股票的框架。注意边界条件的处理和循环的范围

<br><br>

# 贪心算法（各类区间问题）
## [435.无重叠区间.py](435.无重叠区间.py)
将区间[start, end]按照end由小到大的顺序排序，先选定end最小的那个区间x，然后将所有与x相交的区间都去掉。重复该过程直到没有重叠区间

## [452.用最少数量的箭引爆气球.py](452.用最少数量的箭引爆气球.py)
和上一题本质相同，即求无重叠区间的数量

## [1024.视频拼接.py](1024.视频拼接.py)
将区间[start, end]按照start由小到大、start相同end由大到小的顺序排序。首选选出start为0且长度最长的视频，当前视频的结束为curr_end。接着找出所有start小于等于curr_end的视频中end最大的那一个作为下一个被选中的视频，并更新curr_end，重复该过程，直到curr_end大于视频总时长为止。

## [55.跳跃游戏.py](55.跳跃游戏.py)
维护一个farthest变量，随着数组遍历更新，看farthest能不能到达最后一个位置即可

## [45.跳跃游戏-ii.py](45.跳跃游戏-ii.py)
可以转化为区间问题，nums里每个数字其实对应一个区间[i, i + nums[i]]，相当于选出最少的区间个数来覆盖整个区间，这样就类似于1024题了。并且这些区间还是天然按照start由小到大排好序的。贪心算法也就是说在每次能够到达的所有位置中，选择能够跳得最远的那个

## [134.加油站.py](134.加油站.py)
贪心思路：如果选择站点i作为起点「恰好」无法走到站点j，那么i和j中间的任意站点都不可能作为起点。如何判断无法是否可以到达站点j？只需看当前油箱里的总油量是不是大于0

## [1288.删除被覆盖区间.py](1288.删除被覆盖区间.py)
将区间按照start升序、end降序排序，遍历每一个区间，初始end值为0，如果该区间的end比当前的end大，则意味着该区间无法被覆盖，cnt+1且更新end

<br><br>

# 回溯算法
回溯算法和 DFS 算法的细微差别是：回溯算法是在遍历「树枝」，DFS 算法是在遍历「节点」
```
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```
## [46.全排列.py](46.全排列.py)
直接套用回溯模板即可

## [47.全排列-ii.py](47.全排列-ii.py)
由于有重复，那么只需把index加入到visited中即可记录该元素有没有被访问过，最后加入到答案list中时判断一下该组合是否已经存在了即可。
<br>优化方法：剪枝。先将nums排序，剪枝条件为
```
if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
    continue
```
如果这个元素是重复的，且之前和它相同的元素还没有被使用过，那么我们就先暂时不管它，等待它之前的元素先加入排序。如果之前的元素已经被使用过也就是说已经在排序中了，那么我们就继续正常使用这个元素。这样的话可以确保重复元素的相对位置是固定的，减少了重读的排序。

## [51.n-皇后.py](51.n-皇后.py)
路径：board 中小于 row 的那些行都已经成功放置了皇后
选择列表：第row行的所有列都是放置皇后的选择
结束条件：row超过board的最后一行，即 row == len(board)
判断某个位置是否可以放置皇后时，只需判断它的上方，左上和右上是否有皇后，不需要判断下方因为下方还没有放置皇后

## [698.划分为k个相等的子集.py](698.划分为k个相等的子集.py)
https://labuladong.github.io/algo/4/30/105/

## [78.子集.py](78.子集.py)
```
class Solution:
    def dfs(self, nums, start, curr):
        self.ans.append(curr[:])
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, curr + [nums[i]])

    def subsets(self, nums):
        self.ans = []
        self.dfs(nums, 0, [])
        return self.ans
```

## [77.组合.py](77.组合.py)
```
class Solution:
    def dfs(self, n, k, curr, start):
        if len(curr) == k:
            self.ans.append(curr[:])
        for i in range(start, n):
            self.dfs(n, k, curr + [i+1], i+1)
    
    def combine(self, n, k):
        self.ans = []
        self.dfs(n, k, [], 0)
        return self.ans
```

## [40.组合总和-ii.py](40.组合总和-ii.py)
套用框架即可。注意有重复元素，故先将数组排序，然后再使用剪枝逻辑
```
if i > start and nums[i] == nums[i - 1]:
    continue
```
注意组合的剪枝逻辑和全排列的剪枝逻辑的对比

## [39.组合总和.py](39.组合总和.py)
一个元素可用多次，那么只需将数组排序，在回溯下一层时传入start而不是start+1即可

## [37.解数独.py](37.解数独.py)
回溯算法。注意我们只需找到一组解就可以停止，注意一下要在哪里加return。如果没有在找到解后立刻停止，board会被回溯算法还原成初始状态

## [22.括号生成.py](22.括号生成.py)
回溯算法。用left和right分别记录剩余左括号和有括号的个数，终止条件为left == 0 and right == 0. 每次添加括号时需要保证left >= right

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
- [98.验证二叉搜索树.py](98.验证二叉搜索树.py)
- [701.二叉搜索树中的插入操作.py](701.二叉搜索树中的插入操作.py)
- [450.删除二叉搜索树中的节点.py](450.删除二叉搜索树中的节点.py)
- [72.编辑距离.py](72.编辑距离.py)
- [1312.让字符串成为回文串的最少插入次数.py](1312.让字符串成为回文串的最少插入次数.py)
- [47.全排列-ii.py](47.全排列-ii.py)
- [51.n-皇后.py](51.n-皇后.py)
- [698.划分为k个相等的子集.py](698.划分为k个相等的子集.py)
- [494.目标和.py](494.目标和.py)
- [787.k-站中转内最便宜的航班.py](787.k-站中转内最便宜的航班.py)
- [1024.视频拼接.py](1024.视频拼接.py)
- [134.加油站.py](134.加油站.py)