https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l==1:
            return
        j = 0
        for i in range(l):
            if nums[i]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1