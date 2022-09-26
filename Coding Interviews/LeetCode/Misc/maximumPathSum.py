# Definition for a binary tree node.
import math
from turtle import right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    maximumGlobalSum = -math.inf
    path = []
    def maxPathSum(self,root):
        self.maxPathSumRe(root)
        return self.maximumGlobalSum, self.path
        
    def maxPathSumRe(self, root):
        if root is None:
            return (0,[])

        leftPathSum, leftPath = self.maxPathSumRe(root.left)

        leftPathSum = max(leftPathSum,0)

        rightPathSum, rightPath = self.maxPathSumRe(root.right)

        rightPathSum = max(rightPathSum,0)

        #if at any point the path at current node is max we update

        localSum = root.val + leftPathSum + rightPathSum

        if localSum > self.maximumGlobalSum:
            self.maximumGlobalSum = localSum
            self.path = leftPath + [root.val] + rightPath[::-1]

        if leftPathSum > rightPathSum:
             return (root.val + leftPathSum), rightPath + [root.val]
        else:
            return (root.val + rightPathSum), leftPath + [root.val]
       


a = TreeNode(-10)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b
a.right = c
c.left = d
c.right = e

print(Solution().maxPathSum(a))

        
        