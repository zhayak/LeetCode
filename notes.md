# Linked List
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
假设slow走了k步，则fast一定比slow多走了k步，这多走的k步其实就是fast在环里转圈，所以k的值一定是环长度的整数倍。
假设相遇点距环的起点的距离为m，则环的起点距head的距离为k-m，也就是说从 head前进 k-m 步即可到达环起点。同时，如果从相遇点继续前进 k-m 步，也恰好到达环起点。
<br>
<br>

# Template
## 