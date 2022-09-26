def find_paths(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)


def find_paths_recursive(root, sum, currentPath, allPaths):
    currentPath.append(root.value)

    if root.value == sum and root.left == None and root.right == None:
        allPaths.append(list(currentPath))
    
    else:
        find_paths_recursive(root.left, sum-root.value, currentPath, allPaths)
        find_paths_recursive(root.right, sum-root.value, currentPath, allPaths)
    
    del currentPath[-1]