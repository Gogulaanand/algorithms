https://leetcode.com/problems/majority-element/submissions/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums), key=nums.count)


# boyer's moore algorithm
https://leetcode.com/problems/majority-element/discuss/51712/Python-different-solutions/587606