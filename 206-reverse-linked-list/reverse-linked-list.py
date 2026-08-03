# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        curr = head.next

        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        head.next = None
        head = prev

        return head