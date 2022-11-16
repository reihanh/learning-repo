def sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			iteration +=1

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr