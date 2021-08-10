https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''.join(map(str,digits))
        res = int(n)+1
        return list(str(res))