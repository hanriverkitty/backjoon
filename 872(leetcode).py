# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        stack1 = [root1]
        stack2 = [root2]
        while True:
            if len(stack1) == 0:
                break
            node = stack1.pop()
            if node.left == None and node.right == None:
                arr1.append(node)
            elif node.left != None or node.right != None:
                if node.left == None:
                    stack1.append(node.right)
                elif node.right == None:
                    stack1.append(node.left)
                else:
                    stack1.append(node.right)
                    stack1.append(node.left)
        while True:
            if len(stack2) == 0:
                break
            node1 = stack2.pop()
            if node1.left == None and node1.right == None:
                arr2.append(node1)
            elif node1.left != None or node1.right != None:
                if node1.left == None:
                    stack2.append(node1.right)
                elif node1.right == None:
                    stack2.append(node1.left)
                else:
                    stack2.append(node1.right)
                    stack2.append(node1.left)
        print(arr1, "\n", arr2)
        if len(arr1) != len(arr2):
            return False
        for i in range(len(arr1)):
            if arr1[i].val != arr2[i].val:
                return False
        return True
