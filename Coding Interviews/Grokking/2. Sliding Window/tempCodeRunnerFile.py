if min_length > len(str):
        return ""
    
    return str[substr_start: substr_start+min_length]