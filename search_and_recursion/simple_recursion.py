#simple_recursion.py

def factorial(n):
	# Base block
	if n == 1:
		return 1
	# Recursion block
	else:
		return n*factorial(n-1)

print(factorial(6))