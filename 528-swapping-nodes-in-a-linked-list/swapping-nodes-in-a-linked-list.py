# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        right = head

        for i in range(k-1):
            curr = curr.next
        
        left = curr

        while curr.next:
            curr = curr.next
            right = right.next
        
        # We need to swap i and j

        left.val,right.val = right.val,left.val

        return head



