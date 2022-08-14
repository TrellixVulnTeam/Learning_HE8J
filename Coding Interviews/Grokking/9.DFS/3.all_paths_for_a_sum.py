class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths


def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return False
    
    #add current node to the path
    currentPath.append(currentNode.val)

    #if current node is a leaf, and the value is equal to sum
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        #traverse left
        find_paths_recursive(currentNode.left, sum-currentNode.val, currentPath, allPaths)
        find_paths_recursive(currentNode.right, sum - currentNode.val, currentPath, allPaths)
    
    #this is so that when it goes up the recursive stack, our currentpath dont have the currentNode value
    del currentPath[-1]
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Tree has path" + str(find_paths(root, 23)))

main()