# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        ahead = head.next
        prev = head
        prev.next = None
        while ahead:
            head = ahead
            ahead = ahead.next
            head.next = prev
            prev = head
        return head
