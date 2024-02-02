# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = deque([root])
        arr = []
        while True:
            node = queue.popleft()
            if node.val == val:
                return node

            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
            if len(queue) == 0:
                return None
