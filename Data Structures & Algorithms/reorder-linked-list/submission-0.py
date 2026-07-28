# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        jumper = head
        length = 0
        while jumper:
            length += 1
            jumper = jumper.next
        jumper = head
        for _ in range(math.ceil(float(length) / 2) - 1):
            jumper = jumper.next
        temp = jumper.next
        jumper.next = None
        jumper = temp
        prev = None
        while jumper:
            temp = jumper.next
            jumper.next = prev
            prev = jumper 
            jumper = temp
        jumper = head
        while prev:
            temp = jumper.next
            jumper.next = prev
            prev = prev.next
            jumper.next.next = temp
            jumper = jumper.next.next
        
        return









