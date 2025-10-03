# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Now We will implement this using Merge Sort or Divide and Conquer
        Time Complexity in that case would be O(n logn)
        1) Split the list into two halves
        2) merge sorted halves
        '''
        # Base Case
        if not head or not head.next:
            return head
        
        # Find the middle element of the Linked List
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None # To break the list into two Halves

        # Sort each Half
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the sorted list
        return self.merge(left,right)
    
    def merge(self,l,r):
        # here l = head of left sorted linked list and r = head of right half
        d = tail = ListNode()
        while l and r:
            if l.val <= r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next
        if l:
            tail.next = l
        else:
            tail.next = r
        return d.next


