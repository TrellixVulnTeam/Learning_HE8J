'''
given a list of words, we have to find the starting index of the string which has the word as its
substring


'''
def find_word_concatenation(str, words):
    
    if len(words) == 0 or len(words[0]) == 0:
        return []
    
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1
    
    result_indices = []
    words_count = len(words)
    word_length = len(words[0])
    count = words_count

    for i in range((len(str) - words_count*word_length)+1) :
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            word = str[next_word_index: next_word_index + word_length]

            if word not in word_frequency:
                break
            
            #add to words_seen
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            #more of the words in the substring than the acutal one
            if words_seen[word] > word_frequency.get(word, 0):
                break
            
            #if we manage to reach here, means all the words are in, then no extra words
            if j + 1 == words_count:
                result_indices.append(i)
        
    return result_indices


def alt_method(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []
    
    word_frequency = {}
    res = []
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1
    
    result_indices = []
    words_count = len(words)
    word_length = len(words[0])
    count = words_count

    for i in range(0, len(str) - words_count * word_length + 1):
        count = words_count
        temp_map = word_frequency.copy()

        for j in range (0, words_count):
            next_word_index = i + j * word_length
            word = str[next_word_index: next_word_index + word_length]
            
            #dont have such word, or the word already 0
            if (word not in word_frequency or temp_map[word] == 0):
                break

            else:
                temp_map[word] -= 1
                count -= 1
            
        if count == 0:
            res.append(i)
        
    
    return res