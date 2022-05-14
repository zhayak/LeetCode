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

## [27.移除元素.py](27.移除元素.py) [283.移动零.py](283.移动零.py)
与26题思路一致

## [167.两数之和-ii-输入有序数组.py](167.两数之和-ii-输入有序数组.py) [344.反转字符串.py](344.反转字符串.py)
左右两指针，从两侧到中间靠拢

## [5.最长回文子串.py](5.最长回文子串.py)
遍历字符串，以每个字符为中心，使用左右两指针向两侧扩展找到最长回文串。需要注意的是，回文串可以是奇数也可以是偶数个，所以每个中心要考虑到这两种情况。

## [303.区域和检索-数组不可变.py](303.区域和检索-数组不可变.py)
使用前缀和的方法，不用反复进行累加计算，只需在初始化时计算一次即可

<br><br>

# 解题思路
### **化繁为简，重复利用**
将比较复杂的题目想办法转化/分解成简单的题目，利用简单题目的代码<br>
例如：92可直接利用206的代码
### **回文**
寻找回文串是从中间向两端扩展，判断回文串是从两端向中间收缩。对于单链表，无法直接倒序遍历，可以造一条新的反转链表，可以利用链表的后序遍历，也可以用栈结构倒序处理单链表

<br><br>

# Review List
- [25.k-个一组翻转链表.py](25.k-个一组翻转链表.py)
- 