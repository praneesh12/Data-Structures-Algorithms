import time 

def fib(num):
    """
    T -> O(2**n)
    S -> O(n)
    """
    if num<=1: 
        return num
    else:
        return fib(num-1) + fib(num-2)

def fibStack(num):
    """
    T -> O(n)
    S -> O(n)
    """
    seen={}
    for i in range(num):
        if i <= 1:
            if num not in seen:
                seen[i] = 1
        else:
            seen[i] = seen[i-1] + seen[i-2]
        
    return seen[num-1]


def fib_seen(num, seen):
    """
    T -> O(n)
    S -> O(n)
    """
    if seen[num] == -1:
        if num <= 1:
            seen[num] = num
        else:
            return fib_seen(num-1, seen) + fib_seen(num-2, seen) 
    return seen[num]



def fibOpt(num):
    """
    T -> O(n)
    S -> O(1)
    """
    first = 1 # fib(0)
    second = 1 # fib(1)
    if num <= 1:
        return 1
    for i in range(2, num):    
        curr = first+second
        first = second
        second = curr
    return curr
        

if __name__=="__main__":
    
    num = 40
    seen = [-1]*(num+1)
    
    fib(num)
    fibStack(num)
    fib_seen(num,seen)
    fibOpt(num)