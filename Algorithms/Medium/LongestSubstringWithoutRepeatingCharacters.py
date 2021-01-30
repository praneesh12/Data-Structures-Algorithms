class Solution:
    def lengthOfLongestSubstring(self, s):
        
        d = {}
        maxLen = 0
        i = 0
        left=0
        while i < len(s):
            print(left, i, d)
            if s[i] not in d or d[s[i]] < left:
                d[s[i]] = i
                maxLen = max(maxLen, i-left+1)
            
            elif s[i] in d.keys():
                left = d[s[i]]+1
                d[s[i]] = i 

            i+=1
            
        return maxLen
                
s="abcabcbb"
Solution().lengthOfLongestSubstring(s)