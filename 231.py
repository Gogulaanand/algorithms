https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        
        return not (n & (n-1))

https://stackoverflow.com/questions/4678333/n-n-1-what-does-this-expression-do