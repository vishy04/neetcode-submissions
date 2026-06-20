# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        temp_1, temp_2, d1 = list1, list2, dummy

        while temp_1 and temp_2:
            if temp_1.val >= temp_2.val:
                #creating new_node and adding ( O(N) )
                d1.next = temp_2
                temp_2 = temp_2.next

            else:
                d1.next = temp_1
                temp_1 = temp_1.next

            d1 = d1.next
        #leftover checking
        if temp_1 :
            d1.next = temp_1
        elif temp_2 :
            d1.next = temp_2
        else :
            d1.next = None
        
        return dummy.next

