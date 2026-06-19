class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_pro = [1] * n

        for i in range(1, n):
            #i-1 in nums so that the product does not include itself
            pre_pro[i] = nums[i-1] * pre_pro[i-1]

        suf_pro = [1] * n 
        for i in range(n-2, -1, -1):
            suf_pro[i] = nums[i+1] * suf_pro[i+1]

        res =[0] * n
        for i in range(n):
            res[i] = pre_pro[i]*suf_pro[i]
        
        return res