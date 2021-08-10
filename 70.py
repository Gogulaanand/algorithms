https://leetcode.com/problems/climbing-stairs/submissions/


class Solution:
    def climbStairs(self, n: int) -> int:
        m = [0 for _ in range(n+1)]
        m[0] = 1
        m[1] = 1
        for i in range(2,n+1):
            m[i] = m[i-1] + m[i-2]
        return m[-1]