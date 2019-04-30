# Assembling towers of Hanoi using recursion

# Goal: Shift discs from one tower to another
# Rules: There are 3 towers and m discs. Only a smaller disc can come over a disc.
# n -> number of discs

def move_discs(src, dest):
	print('moving disc from {} to {}'.format(src, dest))

def Hanoi(n, src, dest, temp):
	count=0
	if n==1:
		move_discs(src, dest)
	else:
		print(count)
		Hanoi(n-1, src, temp, dest)
		Hanoi(1, src, dest, temp)
		Hanoi(n-1, temp, dest, src)