class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for the end of the valid elements in nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        
        # Pointer for the very end of nums1 (including the padded space)
        p = m + n - 1

        # Compare elements from the back and place the largest at the end of nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 still has elements left, copy them over.
        # (If nums1 has leftovers, they are already sorted and in the correct place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1