class Solution:
    def hasDuplicate(self, nums):
        basket = []
        found = False
        for i in nums:
            if i in basket:
                found = True
            else:
                basket.append(i)
        return(found)           