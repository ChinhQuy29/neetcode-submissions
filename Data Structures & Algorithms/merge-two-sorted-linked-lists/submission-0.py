# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        jumper_res = res
        jumper1 = list1
        jumper2 = list2
        while jumper1 and jumper2:
            if jumper1.val <= jumper2.val:
                jumper_res.next = jumper1
                jumper1 = jumper1.next
                jumper_res = jumper_res.next
            else:
                jumper_res.next = jumper2
                jumper2 = jumper2.next
                jumper_res = jumper_res.next
        
        if jumper1:
            jumper_res.next = jumper1
        
        if jumper2:
            jumper_res.next = jumper2

        return res.next
