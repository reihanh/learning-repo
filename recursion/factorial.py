def iterative(n):
	result = 1

	for i in range(n):
	 	result *= n-i

	return result

def recursive(n):

	if n == 1:
		return n
	else:
		return n * recursiveShort(n-1) 