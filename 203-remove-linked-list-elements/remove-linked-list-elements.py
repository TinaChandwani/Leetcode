# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None :
            return head

        while head is not None and head.val == val:
            head = head.next
        prev = head
        curr = head
        while curr:
            nextt = curr.next
            if curr.val != val:
                prev = curr
            else:
                prev.next = nextt
            curr = nextt
        
        return head
