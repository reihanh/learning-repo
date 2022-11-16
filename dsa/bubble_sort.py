def sort(arr):
	iteration = 0
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			iteration +=1
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr, iteration

			

arr = [9,8,7,6,5,4,3,2,1]

print(sort(arr))