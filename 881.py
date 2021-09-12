https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/


from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        x = Counter(s)
        for k, v in x.items():
            if v==1:
                return s.index(k)
        return -1    



