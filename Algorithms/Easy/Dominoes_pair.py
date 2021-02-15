class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        d = {}
        c = 0
        for i in range(len(dominoes)):
            
            key = (dominoes[i][0], dominoes[i][1])
            
            if key in d:
                d[key] += 1
            
            elif (key[1], key[0]) in d:
                d[(key[1], key[0])] += 1
            
            else:
                d[key] = 1
        pairs = 0
        for k,v in d.items():
            if v > 1:
                pairs += v*(v-1)//2
                
        return pairs
        
dominoes = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
Solution().numEquivDominoPairs(dominoes)