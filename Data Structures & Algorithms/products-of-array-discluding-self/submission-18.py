class Solution:
    def productExceptSelf(self, nums: List[int]):
        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i] = product
            product = product * nums[i]
        product = 1
        i = len(nums) - 1
        while i >= 0:
            output[i] = output[i] * product
            product = product * nums[i]
            i = i - 1
        return output         