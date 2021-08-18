https://leetcode.com/problems/binary-tree-postorder-traversal/

# recursion
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        x = []
        
        return self.dfs(root, x)
        
        
    def dfs(self, root: Optional[TreeNode], x: List[int]) -> List[int]:
        if root:
            self.dfs(root.left, x)
            self.dfs(root.right, x)
            x.append(root.val)
        return x

# iteration
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]