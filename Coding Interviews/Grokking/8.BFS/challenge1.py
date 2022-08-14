from collections import deque
class Treenode:
    def __init__(self, value):
        self.value = value
        self.left, self.right, self.next = None, None, None
    
    def __str__(self):
        return str(self.value)
    
    def print(self):
        curr = self
        while curr:
            print(str(curr.value) + "->" ,end="")
            curr = curr.next
  


def BFS(root):
    if root is None: 
        return None
    queue = deque()
    #push root to queue
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        # if previousNode:
        #     previousNode.next = currentNode
        # previousNode = currentNode
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        currentNode.next = queue[0] if queue else None
    
        

def main():
    root = Treenode(12)
    root.left = Treenode(7)
    root.right = Treenode(1)
    root.left.left = Treenode(9)
    root.right.left = Treenode(10)
    root.right.right = Treenode(5)
    BFS(root)
    root.print()

main()