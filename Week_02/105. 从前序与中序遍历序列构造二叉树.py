# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(p_l, p_r, i_l, i_r):
            if p_l > p_r:
                return None
            p_root = p_l
            i_root = index[preorder[p_root]]
            root = TreeNode(preorder[p_root])
            size_of_left = i_root - i_l
            root.left = build(p_root + 1, p_root + size_of_left, i_l, i_root - 1)
            root.right = build(p_root + size_of_left + 1, p_r, i_root + 1, i_r)
            return root

        index = {ele: i for i, ele in enumerate(inorder)}
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)