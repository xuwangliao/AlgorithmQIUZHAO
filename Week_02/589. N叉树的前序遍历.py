"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        if not root:
            return []
        stack = []
        ans = []
        stack.append(root)

        while stack:
            cur = stack.pop()
            ans.append(cur.val)
            temp = []
            for child in cur.children:
                temp.append(child)
            stack += temp[::-1]

        return ans