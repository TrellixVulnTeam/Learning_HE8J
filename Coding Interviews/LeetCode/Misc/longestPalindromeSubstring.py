def longestPalindrome(s: str) -> str:
        if len(s) == 1:
            return s
        
        maxLen = 0
        res = ""
        for i in range(len(s)):
            l, r = i, i
            #odd palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                    print(res)
                l -= 1
                r += 1

            #even palindrome
            l, r = i, i+ 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                    print(res)
                l -= 1
                r += 1
    
            
        return res
longestPalindrome('babad')