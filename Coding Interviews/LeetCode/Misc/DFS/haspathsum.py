def hasPath(root, sum):
    if root.val == sum and root.left == None and root.right == None:
        return True
    
    #recursively traverse through the neighbours, if one of them is true, return true
    return hasPath(root.left, sum - root.value) or hasPath(root.right, sum - root.value)