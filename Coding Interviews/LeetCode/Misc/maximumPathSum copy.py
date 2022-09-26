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

    def maxPathSum(self,root):
        self.maxPathSumRe(root,[])
        return self.maximumGlobalSum, self.path
        
    def maxPathSumRe(self, root, path):
        if root is None:
            return (0)
        path.append(root.val)
        leftPathSum = max(self.maxPathSumRe(root.left, path),0)
        leftPath = list(path)

        rightPathSum= max(self.maxPathSumRe(root.right, path),0)
        rightPath = list(path)

        #if at any point the path at current node is max we update
        localSum = root.val + leftPathSum + rightPathSum

        if localSum > self.maximumGlobalSum:
            print(leftPath)
            self.maximumGlobalSum = localSum
            self.path = leftPath[:-1:-1] + [rightPath]

        del path[-1]

        if leftPathSum > rightPathSum:
            return (root.val + leftPathSum)
        else:
            return (root.val + rightPathSum)

       


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

        
        