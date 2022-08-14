from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
    

def traversal(root):
    result = deque()

    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            #pop left removes from front, pop right removes from end
            currentNode = queue.popleft()
            #add node to current level
            currentLevel.append(currentNode.value)
            #insert the children into queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel)

    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(traversal(root))

main()