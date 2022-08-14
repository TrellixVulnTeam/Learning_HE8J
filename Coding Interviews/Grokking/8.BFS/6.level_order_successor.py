from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
    

def find_successor(root, given):

    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    while queue:
        #pop left removes from front, pop right removes from end
        currentNode = queue.popleft()       
        #insert the children into queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        if currentNode.value == given:
            break 
            
           
    return queue[0] if queue else None
        

    

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print(find_successor(root,12).value)

main()