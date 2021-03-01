class Solution:
    def merge(self, intervals):
        
        if not intervals: return []
        
        if len(intervals) < 2:
            return intervals

        print("before sort", intervals)
        intervals.sort(key=lambda x: x[0])
        print("after sort", intervals)
        
        merged = []
        cr = 1
        for i in range(len(intervals)-1):
            print("merge list progression->", merged)

            # if the list of merged intervals is empty or
            # if the current interval does not overlap with 
            # the previous, simply append it
            if not merged or intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            # otherwise there is an overlap so we merge the current and previous intervals
            else:
                cr += 1
                merged[-1][1] = max(merged[-1][1], intervals[i][1])            
        return cr 
        

intervals = [[7,10],[2,4]]
s = Solution()
print(s.merge(intervals))

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# s = Solution()
# print(s.merge(intervals))

# intervals = [[1,4],[0,4]]
# s = Solution()
# print(s.merge(intervals))