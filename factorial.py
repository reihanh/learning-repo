number = int(input("Input number: "))

# iterative
def iterative(n):
	result = 1
	# Iterate from 2 for efficiency
	for i in range(2, n+1):
		result *= i

	# alternative readable
	# for i in range(n):
	# 	result *= n-1

	return result
		
print(f"iterative\t: {iterative(number)}")

# recursive
def recursive(n):
	temp = 0
	if n==1:
		return n
	else:
		temp = recursive(n-1)
		temp *= n
	return temp

print(f"recursive\t: {recursive(number)}")

# recursive short
def recursiveShort(n):
	if n == 1: return n
	else: return n * recursiveShort(n-1) 

print(f"recursive2\t: {recursiveShort(number)}")

# Note
"""
Recursive is bad for performance

"""