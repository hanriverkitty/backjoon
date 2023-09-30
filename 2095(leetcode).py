# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cnt = head
        while cnt:
            cnt = cnt.next
            n += 1
        if n == 1:
            head = None
            return
        ahead = head
        for _ in range(0, n // 2 - 1):
            ahead = ahead.next
        ahead.next = ahead.next.next
        return head
