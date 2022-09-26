# def longestPalindrome(s: str) -> str:
#     if len(s) == 1:
#         return True
#     max_length = 1
#     palindrome = ""

#     for i in range(1,len(s) - 1):
#         k = 1
#         r = 1
#         while s[i] == s[i+r]:
#             r += 1

#         while i-k >= 0 and i+k <= len(s) - 1 and s[i-k] == s[i+k]:
#             if k*2 + 1 > max_length:
#                 max_length = k*2 + 1
#                 palindrome = s[i-k: i+k+1]
#                 print(palindrome)
#             k += 1

#     return palindrome

# print(longestPalindrome("bccbc"))

from tokenize import Number


def longestConsecutive(nums) -> int:
    map = {}
    longest = 0
    for number in nums:
        
        if number not in map:
         
            leftRange = map.get(number-1,0)
            rightRange = map.get(number+1,0)
        
            ans = rightRange + leftRange + 1

            map[number] = ans
            map[number - leftRange] = ans
            map[number + rightRange] = ans
          
            longest = max(ans, longest)
        
        
    return longest

print(longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))