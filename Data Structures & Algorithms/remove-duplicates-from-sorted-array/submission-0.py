class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #Since the array is sorted common lies adjacent
        #I need to move to the last of the common element 
        #and swap(equate is better) it with the first non common element
        # I will put left at last duplicate element 
        # Then move right till I reach a non-duplicate ele
        left = right = 0
        nums_length = len(nums)
        while  right < nums_length:
            #left = right not vice-versa
            nums[left] = nums[right]
            #only move right to get first non-duplicate
            while right < nums_length and nums[right] == nums[left]:
                right += 1
            #moves left to the last duplicate
            left += 1
        return left 
        """
        Dry Run:
          nums=[2   10  30  10  30  30]
                            l
                                    r
        """

        