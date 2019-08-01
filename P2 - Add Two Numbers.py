#Question Link - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ln = ListNode(0)        #head node
        tmp_ptr = ln            #iterator node
        carry = 0
        while l1 or l2 or carry:
            sum1 = self.get_digit_from_listnode(l1) + self.get_digit_from_listnode(l2) + carry            
            digit = sum1 % 10       
            carry = sum1 // 10
            
            lnode = ListNode(digit)
            tmp_ptr.next = lnode
            tmp_ptr = lnode
            
            l1 = self.get_next_node(l1)
            l2 = self.get_next_node(l2)
    
        return ln.next
            
    def get_digit_from_listnode(self, listnode):
        '''This function is to handle edge case i.e no list empty or smaller than other'''
        return listnode.val if listnode else 0
    
    def get_next_node(self, listnode):
        '''This function is to handle edge case i.e no list empty or smaller than other'''
        return listnode.next if listnode else None   