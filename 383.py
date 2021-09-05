https://leetcode.com/problems/ransom-note/submissions/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        x = Counter(magazine)
        y = Counter(ransomNote)
        for k in y.keys():
            if y[k] > x[k]:
                return False
        return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)