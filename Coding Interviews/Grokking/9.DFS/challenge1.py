class TreeNode:
    def __init__(self, val, left= None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeDiameter: 
    
    def __init__(self):
        self.diameter = 0
    
    def find_diameter(self, root):
        self.calculateHeight(root);
        return self.diameter
    
    def calculateHeight(self, currentNode):
        if currentNode is None: return 0
        
        leftTreeHeight = self.calculateHeight(currentNode.left)
        rightTreeHeight = self.calculateHeight(currentNode.left)

        diameter = leftTreeHeight + rightTreeHeight + 1

        self.diameter = max(diameter, self.diameter)
        
        return max(leftTreeHeight, rightTreeHeight) + 1