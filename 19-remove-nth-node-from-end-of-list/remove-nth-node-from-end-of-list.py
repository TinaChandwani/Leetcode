# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None :
            return head
        count = 1
        
        def reverseList(head):
            current = head
            prev = None
            while current:
                nextt = current.next
                current.next = prev
                #Update
                prev = current
                current = nextt
            return prev

        head1 = reverseList(head)
        d = ListNode()
        d.next = head1
        current1 = head1
        prev1 = d
        while current1 and count < n:
            prev1 = current1
            current1 = current1.next
            count += 1
        # Deleting a Node
        if current1:
            prev1.next = current1.next
            current1.next = None

        ansnode = reverseList(d.next)

        return ansnode