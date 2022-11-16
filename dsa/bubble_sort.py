def sort(arr):
	for i in range(len(arr)):

		for i in range(len(arr)-1):
			if arr[i]>arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

	return arr

			

arr = [6,5,3,1,8,7,2,4]
arr = sort(arr)

print(arr)