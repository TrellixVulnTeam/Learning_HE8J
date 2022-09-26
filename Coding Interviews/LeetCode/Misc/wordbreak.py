
from collections import *
def wordBreak(s, wordDict) -> bool:
    newDict = set()
    for word in wordDict:
        newDict.add(word)

    windowStart = 0
    for windowEnd in range(0, len(s) + 1):
        print(windowStart)
        print(windowEnd)
        word = s[windowStart:windowEnd]
        print(word)
        #let's say 0:6 means 0-5 is the word, we then update windowstart to 5+1, i.e. 6
        if word in newDict:
            windowStart = windowEnd
    
    return windowStart == len(s)

# print(wordBreak("aaaaaaa",["aaaa","aaa"]))

def wordBreakBFS(s, wordDict):
    lengthlist = []
    for word in wordDict:
        lengthlist.append(len(word))

    visited = set()
    queue = deque()
    queue.append((0))
    while queue:
        start = queue.popleft()
        if start not in visited:
            visited.add(start)
            for end in range(start+1, len(s) + 1): #for length in lengthlist:
                word = s[start: end]                #word = s[start: start+length]
                if word in wordDict:
                    queue.append(end)
                    if end == len(s):
                        return True
    
    return False
# print(wordBreakBFS("aaaaaaa",["aa","aaa"]))

def wordBreakDP(s, wordDict):
    n = len(s)
    dp = [False] * (n+1) #if length is 8, n+1 is 9, means dp[8] is last one, means
    dp[0] = True

    wordNewDict = set(wordDict)
    for end in range(1, n+1): #max end is n, i.e. 8
        for word in wordNewDict:
            if dp[end - len(word)] and s[end - len(word): end] == word:
                dp[end] = True
    print(dp)
    return dp[-1] == True

print(wordBreakDP("catsandog",["cats","dog","sand","and","cat"]))
                    