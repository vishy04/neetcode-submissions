class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        no_of_conc = 2
        ans = []
        while no_of_conc > 0 :
            for num in nums:
                ans.append(num)
            no_of_conc -=1
        return ans

