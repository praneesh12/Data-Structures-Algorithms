# Implement strStr()
# Solution
# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # if len(needle) == 0:
        #     return 0
        # j=0
        # for i in range(len(haystack)):
        #     if haystack[i] == needle[j]:
        #         if haystack[i:i+len(needle)] == needle:
        #             return i
        # return -1
        
        # return 0 if needle=="" else haystack.find(needle)
        
        if needle == '' : return 0
        if haystack == '' or needle not in haystack: return -1
	
        a = haystack.lower().replace(needle,'A')
        for i in range(len(a)):
            if a[i] == 'A':
                break
        return i