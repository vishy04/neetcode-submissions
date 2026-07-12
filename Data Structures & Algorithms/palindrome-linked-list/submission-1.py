# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # move to middle reverse second half
        #moving to the middle node
        mid = fast = head

        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        # starting from mid reverse
        """
        1   2   2   1           1   2   3   2   1
                s                       s
                        f                       f
        """
        rev_head = self.reverse(mid)

        """
        head:         1 -> 2                   1 -> 2
                            \                         \
                             3 -> None                 2 -> None
                            /                         /
        rev_head:     1 -> 2                        1
        """
        #compare both list until the first ends
        temp = head
        #we did not use while temp because it fails for even number of nodes
        while rev_head:
            if temp.val != rev_head.val:
                return False
            temp = temp.next
            rev_head = rev_head.next
        
        return True
    def reverse(self, start):
        prev = None
        curr = start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        #prev is the head of new_ll
        return prev 
