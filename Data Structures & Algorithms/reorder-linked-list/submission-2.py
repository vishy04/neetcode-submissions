# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we split in two half
        # slow-fast pointer

        start = end = head

        while end.next and end.next.next:
            end = end.next.next
            start = start.next

        # reverse the second half

        l2_before = start.next
        # breaking the two ll
        start.next = None

        # prev ends on the head of reversed ll

        l2 = self.reverse(l2_before)
        l1 = head
        # merge them

        while l1 and l2:
            next1, next2 = l1.next, l2.next

            l1.next, l2.next = l2, next1

            l1, l2 = next1, next2

    def reverse(self, head: Optional[ListNode]) -> None:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
