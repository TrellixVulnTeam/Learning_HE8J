def groupAnagrams(words):
    # map = {}

    # for word in words:
    #     freq_map = [0 for i in range(26)]
    #     for char in word:
    #         freq_map[ord(char) - ord('a')] += 1
    #     string_map = str(freq_map)  
        
    #     if string_map not in map:
    #         map[string_map] = [word]

    #     else:
    #         templist = map[string_map]
    #         templist.append(word)
    #         map[string_map] = templist
    #     return list(map.values())
    
    map = {}
    for word in words:
        sortedWord = ''.join(sorted(word))   
        if sortedWord in map:
            map[sortedWord] += [word]
        else:
            map[sortedWord] = [word]  
        print(map)

    return list(map.values())





print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

        
#O(n) - O(m)