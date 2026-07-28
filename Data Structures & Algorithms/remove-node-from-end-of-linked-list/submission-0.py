# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        jumper = head
        length = 0
        while jumper:
            jumper = jumper.next
            length += 1
        jumper = head
        if length - n < 1:
            head = head.next
        else:
            for i in range(length - n - 1):
                jumper = jumper.next
            jumper.next = jumper.next.next
        return head
        
