# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        '''
        U -> Basically you have reorder without using any other ListNode or any dummy node you need to achieve this using in-place
        P ->
        1) Find the middle of the Linked List
        2) Reverse the Linked List after the middle
        3) Then i = 0 and j = middle(start of the second half)
        4) Connect these two nodes, whatever connection they currently have in the orignal array store them using the temp variables
        '''
        if head == None or head.next == None:
            return
        def middle(head):
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        middleEle = middle(head)
        prev = None
        current = middleEle.next
        middleEle.next = None
        
        while current:
            nextt = current.next
            current.next = prev
            #Update
            prev = current
            current = nextt
        i = head
        j = prev

        while j:
            temp1 = i.next
            temp2 = j.next
            i.next = j
            j.next = temp1
            i = temp1
            j = temp2