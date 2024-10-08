# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.dfs(root, targetSum)

    def dfs(self, node, remainingSum):
        if not node.left and not node.right:
            return remainingSum == node.val

        remainingSum -= node.val

        l_has_sum = self.dfs(node.left, remainingSum) if node.left else False
        r_has_sum = self.dfs(node.right, remainingSum) if node.right else False

        return l_has_sum or r_has_sum