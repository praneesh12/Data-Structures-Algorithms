def pascal(i,j):
    if j==i or j==1:
        return 1
    else:
        return pascal(i-1, j-1) + pascal(i-1,j)
    
pascal(10,5)  


class Solution:
    def pascal(self, row, col):
        if row == col or col == 1:
            return 1
        else:
            return self.pascal(row-1, col-1) + self.pascal(row-1, col)
        
    def getRow(self, rowIndex: int):
        if rowIndex <= 1:
            return [1]*(rowIndex+1)
        
        res = []
        for idx in range(1,rowIndex+1):
            val = self.pascal(rowIndex+1, idx)
            res.append(val)
            
        res.append(1)
        return res
            
        
s = Solution()

print(s.getRow(3), end='')
