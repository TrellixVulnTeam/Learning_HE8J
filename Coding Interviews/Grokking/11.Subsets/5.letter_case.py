def letter_case_permutations(text:str):
    permutations = []
    permutations.append(text)
    
    for i in range(len(text)):
        if text[i].isalpha():
            n = len(permutations)
            for j in range(n):
                currentPerm = list(permutations[j])
                currentPerm[i] = currentPerm[i].swapcase()
                permutations.append(''.join(currentPerm))
    
    return permutations