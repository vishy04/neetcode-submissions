class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Intuition:
        We use a three-pointer approach, working backwards from the end of the arrays to avoid overwriting elements in `nums1` that haven't been sorted yet.

        1. Pointer `x` starts at the end of the actual elements in `nums1` (index m - 1).
        2. Pointer `y` starts at the end of `nums2` (index n - 1).
        3. Pointer `z` starts at the very end of `nums1`'s total allocated space (index m + n - 1).

        We iterate backwards with `z`. At each step, we compare the elements at `x` and `y`, pick the larger of the two, and place it at position `z`. We then decrement `z` along with whichever pointer (`x` or `y`) had the larger element.

        If `y` goes out of bounds first, we can break early, as the remaining elements in `nums1` are already in their correct, sorted positions.
        """

        x, y, z = m - 1, n - 1, m + n - 1

        # while y fails at y == 0
        while y >= 0:  
            # if x reaches end of list1 before y then we need consider that in while
            if x >= 0 and nums1[x] >= nums2[y]:
                nums1[z] = nums1[x]
                z -= 1
                x -= 1
            else:
                nums1[z] = nums2[y]
                z -= 1
                y -= 1
