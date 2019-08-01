#Question Link - https://leetcode.com/problems/merge-two-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
	#if empty linkedlist passed
        if l1 is None: return l2
        if l2 is None: return l1
        
	  ln = ListNode(0)		#creating a linkedlist
        head = ln
        while l1 and l2:		#storing the values
            if(l1.val <= l2.val):
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
#storing the remaining values
        head.next = l1 if l2 is None else l2
        return ln.next
                