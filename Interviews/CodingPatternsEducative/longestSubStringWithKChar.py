
def longestSubstringWithKChar(s, k):
    if not s:
        return s
    
    start = 0
    uni = dict()
    max_len = 0
    
    for end in range(len(s)):
        
        if s[end] not in uni:
            uni[s[end]] = 0      
        uni[s[end]] += 1
            
        if len(uni)>k:
            uni[s[start]] -= 1
            if uni[s[start]] == 0:
                del uni[s[start]]
            start += 1
        
        if end+1-start > max_len:
            max_len = end+1-start
    
    return max_len