https://leetcode.com/problems/squares-of-a-sorted-array/

import collections
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                ans.appendleft(left * left)
                l += 1
            else:
                ans.appendleft(right * right)
                r -= 1
        return list(ans)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])