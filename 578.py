https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = collections.Counter(nums)
        for v in x.values():
            if v>1:
                return True
        return False