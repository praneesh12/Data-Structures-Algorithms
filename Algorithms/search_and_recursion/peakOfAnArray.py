def peak(arr):
    
    """ Time O(n) using Linear Scan
       if arr[i-1] < arr[i] < arr[i+1] then arr[i] is peak
       return all such peaks
    """ 
    res=[]
    i=0
    
    while i<len(arr):
        
        if i==0 and arr[i] > arr[i+1]:
            res.append(arr[i])
        elif i==len(arr)-1 and arr[i] > arr[i-1]:
            res.append(arr[i])
        else:
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                res.append(arr[i])
        i+=1
    return res 


def peakBinarySearch(arr):
    
    """[2,4,3,6,1,5]->[4,6,5]"""
    l = 0
    r = len(arr)-1
    res = []
    while l<r:
        mid = (l+r)//2
        if arr[mid] > arr[mid+1]:
            r = mid
            res.append(r)
        else:
            l = mid+1
            res.append(l)
    return res
             
arr = [2,4,3,6,1,5]
print(peak(arr))   
print("Peak of an array using Binary Search")
print(peakBinarySearch(arr))