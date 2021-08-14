https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        x = [i for i in x if i!='']
        return len(x[-1])