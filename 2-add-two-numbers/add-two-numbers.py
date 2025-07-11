# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        carry = 0
        d = ListNode()
        tail = d

        while head1 or head2:
            if head1:
                firstElement = head1.val
            else:
                firstElement = 0 
            secondElement = head2.val if head2 else 0
            print(f'first {firstElement} and second {secondElement}')
            add = firstElement + secondElement + carry
            print(f'Add {add}')
            carry = add // 10
            add = add % 10
            dadd = ListNode(add)
            tail.next = dadd
            tail = tail.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        if carry:
            tail.next = ListNode(carry)
        
        
        return d.next