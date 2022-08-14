class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    if not root:
        return len(sequence) == 0

    return find_path_recursive(root, sequence, 0)

def find_path_recursive(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return False
    
    seqLength = len(sequence)
    if sequenceIndex >= seqLength or currentNode.val != sequence[sequenceIndex]:
        return False
    
    if currentNode.left is None and currentNode.right is None:
        return True
    
    return find_path_recursive(currentNode.left, sequence, sequenceIndex+1) or find_path_recursive(currentNode.right, sequence, sequenceIndex+1) 

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print(find_path(root, [1,0,3]))

main()