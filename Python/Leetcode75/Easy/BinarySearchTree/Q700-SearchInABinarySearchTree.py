# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val == val:
            return root

        sub_tree = None
        if root.val > val:
            sub_tree = self.searchBST(root.left, val)
        else:
            sub_tree = self.searchBST(root.right, val)
        return sub_tree