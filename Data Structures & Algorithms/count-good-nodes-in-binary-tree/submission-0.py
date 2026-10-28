# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal) -> int:
            if node is None:
                return 0
            goodNode = 0
            if node.val >= maxVal:
                goodNode += 1
            newMax = max(node.val, maxVal)
            leftCount = dfs(node.left, newMax)
            rightCount = dfs(node.right, newMax)
            
            return goodNode + leftCount + rightCount

        return dfs(root, root.val)
