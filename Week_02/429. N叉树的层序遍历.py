"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                temp.append(cur.val)
                for child in cur.children:
                    queue.append(child)
            ans.append(temp)
        return ans