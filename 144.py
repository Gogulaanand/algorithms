https://leetcode.com/problems/binary-tree-preorder-traversal/

# recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        x = []
        return self.calculate(root, x)
        
    def calculate(self, root: Optional[TreeNode], x: List[int]) -> List[int]:
        if root:
            x.append(root.val)
            self.calculate(root.left, x)
            self.calculate(root.right, x)
        return x

# iteration
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
                
        return res