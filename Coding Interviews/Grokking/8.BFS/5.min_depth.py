from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
    

def find_min_depth(root):
    depth = 0

    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    while queue:
        depth += 1
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            #pop left removes from front, pop right removes from end
            currentNode = queue.popleft()
            #add node to current level
            currentLevel.append(currentNode.value)
            if not currentNode.left and not currentNode.right:
                return depth

            #insert the children into queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
            
           
        
        

    return depth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(find_min_depth(root))

main()