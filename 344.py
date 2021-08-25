https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        l = len(s)
        if l<2:
            return s
        for i in range(l//2):
            s[i], s[-i-1] = s[-i-1], s[i]

class Solution:
    def reverseString(self, s: List[str]) -> None:
      s.reverse()