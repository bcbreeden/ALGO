def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    
    window = (len(s)-1)
    iterations = 0
    for _ in s:
        window = window - iterations
        s_index = 0
        while window <= len(s):
            substring = s[s_index:window]
            if substring == substring[::-1]:
                return substring
            else:
                s_index += 1
                window += 1
        iterations += 1
    return s[0]


print(longestPalindrome('babad')) #bab or aba
print(longestPalindrome('cbbd')) #bb
print(longestPalindrome('abb'))
print(longestPalindrome('abcda'))