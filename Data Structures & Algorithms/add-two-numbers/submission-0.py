# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        jumper = res
        carry = 0
        while l1 and l2:
            sum_digits = l1.val + l2.val + carry
            new_node = ListNode(sum_digits % 10)
            carry = sum_digits // 10
            jumper.next = new_node
            jumper = jumper.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            s = l1.val + carry
            jumper.next = ListNode(s % 10)
            carry = s // 10
            jumper = jumper.next
            l1 = l1.next
        
        while l2:
            s = l2.val + carry
            jumper.next = ListNode(s % 10)
            carry = s // 10
            jumper = jumper.next
            l2 = l2.next
        
        if carry:
            jumper.next = ListNode(1)

        return res.next
            