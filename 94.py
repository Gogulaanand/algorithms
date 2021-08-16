https://leetcode.com/problems/binary-tree-inorder-traversal/

# recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        x = []
        return self.calculate(root, x)
    
    def calculate(self, root: Optional[TreeNode], x: List[int]) -> None:
        if root:
            self.calculate(root.left, x)
            x.append(root.val)
            self.calculate(root.right, x)
        return x
        

# Iteration

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []        
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res