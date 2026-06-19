# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # reverse the ll from [left,right]
        # storing before_start and after_end(elegantly with start)
        # left = 2 , right = 4 ( 1 based indexing )
        #
        dummy = ListNode(0)
        dummy.next = head
        before_start = dummy

        # go before start
        # [1,2,3,4,5]
        #  ^        <-before_start
        for _ in range(left - 1):
            before_start = before_start.next

        start = before_start.next
        # reversal
        # [1,2,3,4,5]
        #    ^        <-start
        curr = start
        prev = None
        # [1,2,3,4,5]
        #    ^ ^        <-curr , next_node , prev -> None
        for _ in range(right - left + 1):  # runs twice(4-2) # error_1 r-l+1
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        #[1,2,3,4,5]
        # ^     ^ ^ -> before_start, prev , curr
        
        before_start.next = prev
        start.next = curr

        return dummy.next


