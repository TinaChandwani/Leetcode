class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prefixProd = -999999
        max_suffixProd = -999999
        maxEle = -999999

        p_currProd = 1
        s_currProd = 1
        for i in range(len(nums)):
            maxEle = max(maxEle, nums[i])
            p_currProd = p_currProd * nums[i]
            s_currProd = s_currProd * nums[len(nums)-i-1]
            max_prefixProd = max(p_currProd, max_prefixProd)
            max_suffixProd = max(s_currProd, max_suffixProd)
            if p_currProd == 0:
                p_currProd = 1
            if s_currProd == 0:
                s_currProd = 1
        
        return max(max_prefixProd, max_suffixProd, maxEle)
