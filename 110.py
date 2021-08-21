https://leetcode.com/problems/balanced-binary-tree/submissions/

class Solution:
    def __init__(self):
        self.flag = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        self.height(root)
        return self.flag
        
    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh-rh) > 1:
            self.flag = False
        return max(lh, rh)+1
        