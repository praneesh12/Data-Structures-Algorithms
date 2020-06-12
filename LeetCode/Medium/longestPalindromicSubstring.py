def isPalindrome(s):
    
    i=0
    j=len(s)-1
    
    while i < j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            return False
    return True 


def longestPalindromicSubstring(s):
    i = 0
    j = len(s)-1
    
    while i<j:
        
        if s[i] == s[j]:
            print(s[i:j])
            if isPalindrome(s[i:j]):
                return s[i:j]
            else:
                i+=1
                j-=1
        else:
            i+=1
    return False

longestPalindromicSubstring(s)