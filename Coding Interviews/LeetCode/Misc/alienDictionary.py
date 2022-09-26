from collections import *

def alienDict(wordsList):
    
    inDegree = {}
    graph = {}

    for word in wordsList:
        for char in word:
            inDegree[char] = 0
            graph[char] = set()
    
    for i in range(len(wordsList) - 1):
        word1, word2 = wordsList[i], wordsList[i+1]
        for j in range(min(len(word1), len(word2))):
           parent, child = word1[j], word2[j]
           if parent != child:
            if child not in graph[parent]:
                graph[parent].add(child)
                inDegree[child] += 1
            break
    
    source = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            source.append(key)
    res = []
    while source:
        current = source.popleft()
        res.append(current)
        for children in graph[current]:
            inDegree[children] -= 1
            if inDegree[children] == 0:
                source.append(children)
    
    print(graph)
    if len(inDegree) != len(res):
        return ""
 
    return res

print(alienDict(['w','q', 'qwe', 'qwr']))