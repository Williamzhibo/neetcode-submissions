# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return 
        
        # STEP 1: Find the middle of the list
        midpoint = head
        curr = head.next
        while curr is not None and curr.next is not None:
            midpoint = midpoint.next
            curr = curr.next.next
        
        # STEP 2: Reverse second half of the list
        curr = midpoint.next
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        midpoint.next = None  # Cut off the first half cleanly
        
        # STEP 3: Merge two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
