def sort(arr):
	iteration = 0
	for i in range(len(arr)):
		for i in range(len(arr)-1):
			iteration +=1
			if arr[i]>arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]

	return arr, iteration

			

arr = [9,8,7,6,5,4,3,2,1]

print(sort(arr))