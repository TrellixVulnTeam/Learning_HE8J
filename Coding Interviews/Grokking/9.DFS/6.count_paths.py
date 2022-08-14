class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

def count_paths(root, sum):
    return count_paths_recursive(root, sum, [])
     


def count_paths_recursive(currentNode, sum, currentPath):
    if currentNode is None:
        return False
    
    #add current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0,0

    #find the sums of all subpaths in the current path list
    for i in range(len(currentPath)- 1 , -1, -1):
        pathSum += currentPath[i]
        #if any of subpath's sum is sum, add to pathcount
        if pathSum == sum:
            pathCount += 1

        #traverse left
    pathCount += count_paths_recursive(currentNode.left, sum-currentNode.val, currentPath)
    pathCount += count_paths_recursive(currentNode.right, sum - currentNode.val, currentPath)

    del currentPath[-1]
    return pathCount
    
    #this is so that when it goes up the recursive stack, our currentpath dont have the currentNode value
    del currentPath[-1]
def main():
    root = TreeNode(12)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Tree has path" + str(count_paths(root, 13
    )))

main()