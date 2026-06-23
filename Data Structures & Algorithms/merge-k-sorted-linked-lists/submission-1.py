# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, id(node), node))
        
        dummy = ListNode(-1)
        current = dummy
        
        while heap:
            val, guid , node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val,id(node.next), node.next))
        
        return dummy.next


