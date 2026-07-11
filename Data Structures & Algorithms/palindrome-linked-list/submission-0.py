# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # store nodes in array
        palindrome = []
        curr = head
        while curr:
            palindrome.append(curr)
            # you do not move curr -> next (common error)
            curr = curr.next

        left, right = 0, len(palindrome) - 1
        while left < right:
            if palindrome[left].val != palindrome[right].val:
                return False
            left += 1
            right -= 1

        return True
