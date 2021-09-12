https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
            