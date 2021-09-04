https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        x = Counter(s)
        for k, v in x.items():
            if v==1:
                return s.index(k)
        return -1    