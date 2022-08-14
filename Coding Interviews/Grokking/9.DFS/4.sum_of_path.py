class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sum(paths):
    total_sum = 0
    for path in paths:
        print(path)
        path_sum = 0
        for i in range(len(path)):
            path_sum += path[i]*(10**(len(path) -1 -i))
        total_sum += path_sum
    return total_sum

def find_paths(root):
    allPaths = []
    find_paths_recursive(root, [], allPaths)
    return allPaths



def find_paths_recursive(currentNode, currentPath, allPaths):
    if currentNode is None:
        return False
    
    #add current node to the path
    currentPath.append(currentNode.val)

    #if current node is a leaf
    if currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        #traverse left
        find_paths_recursive(currentNode.left, currentPath, allPaths)
        find_paths_recursive(currentNode.right, currentPath, allPaths)
    
    #this is so that when it goes up the recursive stack, our currentpath dont have the currentNode value
    del currentPath[-1]

### Modal Answers
def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_numbers(root, 0)

def find_root_to_leaf_path_numbers(currentNode, pathSum):
    if currentNode is None:
        return 0
    
    pathSum = 10 * pathSum + currentNode.val

    if currentNode.left is None and currentNode.right is None:
        return pathSum
    
    return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)
def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(sum(find_paths(root)))
    print(find_sum_of_path_numbers(root))

main()

