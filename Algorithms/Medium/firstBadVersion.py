# firstBadVersion.py

isBadApi = [False, False, False, False, False, False]

def firstBadVersion_binarySearch(isBadApi):
    low = 0
    high = len(isBadApi)-1
    print(low)
    while low <= high:
        mid = (low+high)//2
        
        if isBadApi(mid):
            right = mid
        
        else:
            low = mid+1
    return low

print(firstBadVersion_binarySearch([False, False, False, False]))
