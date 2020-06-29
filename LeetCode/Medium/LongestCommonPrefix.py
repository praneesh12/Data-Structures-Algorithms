LongestCommonPrefix.py


"""
Horizontal Scanning: LCP(LCP(LCP...LCP(s1,s2),s3)...sn)

Time Complexity: O(S), S= sum of all characters in the lists of strings
Space Complexity: O(1)

"""

def longestCommonPrefix(strs):
    lcp_string = strs[0]
    
    for i in range(len(strs)):
        lcp_string = LCP(lcp_string, strs[i])
    return lcp_string

def LCP(s1, s2):
    j=0
    i=0
    return_string = ""
    print(s1,s2)
    while i < len(s1) and j < len(s2):
        print(s1[i], s2[j])
        if s1[i] == s2[j]:
            return_string += s2[i]
            i+=1
            j+=1
        else: 
            return return_string
    
    return return_string 



search = strs[0]

for i in range(len(strs)):
    
    search = LCP(search, strs[i])
return search


def LCP(s1, s2):
    
    i = 0
    j = 0
    returnString = ""
    while i < len(s1) and j < len(s2):
        
        if s1[i] == s2[j]:
            returnString += s2[i]
            i+=1
            j+=1
        else:
            returnString
            
    return returnString
    
            