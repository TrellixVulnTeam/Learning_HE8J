from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right, self.next = None, None, None
    
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.value) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

def connect_level_order(root):
    if root is None:
        return 
    
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        previousNode = None
        for _ in range(levelSize):
            #pop left removes from front, pop right removes from end
            currentNode = queue.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode
            #add node to current level
            #insert the children into queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(connect_level_order(root))
    root.print_level_order()

main()