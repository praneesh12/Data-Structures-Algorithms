TwoSumII(preSorted).py

def twoSum_using2pointers(numbers, target):
	"""
	Time Complexity: O(n)
	Space Complexity: O(1)
	"""
	# Using 2 two pointer approach
    i=0
    j=len(numbers)-1

    while i < j:
        if (numbers[i] + numbers[j])== target:
            return i+1, j+1
        elif (numbers[i]+numbers[j]) < target:
            i+=1
        else:
            j-=1
    return []

def twoSum_usingDict(numbers, target):	
	"""
	Time : O(n)
	Space: O(n)
	"""

	d={}
    for i in range(len(numbers)):
        if numbers[i] not in d.keys() or (i != numbers.index(target-numbers[i]) ):
            d[numbers[i]] = target-numbers[i]

        if numbers[i] in d.values():
            return numbers.index(target-numbers[i]), i
    return []