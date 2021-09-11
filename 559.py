https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/559/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join([str(i) for i in digits])
        n = int(s)
        return list(str(n+1))


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                return digits
        digits.insert(0, 1)
        return digits
                