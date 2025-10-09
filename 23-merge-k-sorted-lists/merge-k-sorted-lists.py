# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Solve using Heap => (node.val,index,node)
        '''
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        dummy = ListNode()
        tail = dummy
        heap = []
        # Just out the first element of all the list into heap
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        while heap:
            snode_val,si,snode = heapq.heappop(heap)
            tail.next = snode
            tail = tail.next
            if snode.next:
                heapq.heappush(heap,(snode.next.val,si,snode.next))
        return dummy.next