# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        jumper = head
        while jumper.next:
            jumper = jumper.next
        reversed_head = jumper
        dummy = jumper
        while dummy != head:
            jumper = head
            while jumper.next != dummy:
                jumper = jumper.next
            dummy.next = jumper
            dummy = dummy.next
        dummy.next = None
        return reversed_head



