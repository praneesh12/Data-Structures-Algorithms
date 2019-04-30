# Fibbonacci recursion - Da Vinci Code

def fibbonacci(n):
	# Base Case
	if n == 0:
		return 0
	elif n == 1:
		return 1
	# Recursion Case
	else:
		return fibbonacci(n-1) + fibbonacci(n-2)