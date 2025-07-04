# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findReverse(self,head):
        prev = head
        curr = head.next
        while curr:
            nextt = curr.next
            curr.next = prev
            #update
            prev = curr
            curr = nextt
        head.next = None
        head = prev
        return head

    def findMiddle(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        Algorithm :-
            1. Find the Middle of the Linked List
            2. reverse the second half of the linked list
            3. compare val by value the first half and the second halve
        '''
        if head == None or head.next == None:
            return True
        middle = self.findMiddle(head)
        new_head = self.findReverse(middle.next)

        while new_head:
            if new_head.val != head.val:
                return False
            new_head = new_head.next
            head = head.next
        return True