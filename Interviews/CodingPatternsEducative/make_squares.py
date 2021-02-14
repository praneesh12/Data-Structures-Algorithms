def make_squares(arr):
    squares = []
    
    i = 0
    while i<len(arr):
        if arr[i]<0:
            i+=1
        else:
            break
    
    j = i+1
    while i>=0 and j<len(arr):
        
        if arr[i]**2 < arr[j]**2:
            squares.append(arr[i]**2)
            i-=1
        elif arr[i]**2 > arr[j]**2:
            squares.append(arr[j]**2)
            j+=1
        else:
            squares.append(arr[i]**2)
            squares.append(arr[j]**2)
            i-=1
            j+=1
            
    while i>=0:
        squares.append(arr[i]**2)
        i-=1
    while j<len(arr):
        squares.append(arr[j]**2)
        j+=1
    
    return squares
