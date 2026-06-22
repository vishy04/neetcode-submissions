# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head
        # we could remove head so dummy
        dummy = ListNode(0)
        dummy.next = head
        p2 = dummy

        for _ in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next
        
        #p2 on node before last n
        #removal
        target = p2.next
        p2.next = target.next
        target.next = None
        
        return dummy.next
