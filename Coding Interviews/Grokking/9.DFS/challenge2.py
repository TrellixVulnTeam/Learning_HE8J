import math


class TreeNode:
    def __init__(self, val, left= None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaximumSum: 
    
    def find_max_sum(self, root):
        self.globalMaxSum = -math.inf
        self.calculateMaxSum(root)
        return self.globalMaxSum
    
    def calculateMaxSum(self, currentNode):
        if currentNode is None: return 0
        
        leftTreeMaxSum = self.calculateMaxSum(currentNode.left)
        rightTreeMaxSum = self.calculateMaxSum(currentNode.left)

        leftTreeMaxSum = max(leftTreeMaxSum , 0)
        rightTreeMaxSum = max(rightTreeMaxSum, 0)

        localMaxSum = leftTreeMaxSum + rightTreeMaxSum + currentNode.val

        self.globalMaxSum = max(self.globalMaxSum, localMaxSum)
        
        return max(leftTreeMaxSum, rightTreeMaxSum) + currentNode.val