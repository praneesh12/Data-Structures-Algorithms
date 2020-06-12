class Solution:
    def groupAnagrams(self, strs):

        anagrams = dict()
        j=0
        group = ""
        for i in range(len(strs)):
            group = ''.join(sorted(list(strs[i])))
            if group not in anagrams.keys():
                anagrams[group] = [strs[i]]
            else:
                anagrams[group].append(strs[i])
        
        return list(anagrams.values())
    
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution().groupAnagrams(strs)