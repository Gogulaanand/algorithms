https://leetcode.com/problems/merge-two-binary-trees/

# dfs, recursive
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        
        return root1


# bfs, iterative
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not(root1 and root2):
            return root1 or root2
        
        q1, q2 = collections.deque([root1]), collections.deque([root2])
        
        while q1 and q2:
            node1, node2 = q1.popleft(), q2.popleft()
            if node1 and node2:
                node1.val += node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)

                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            
        return root1