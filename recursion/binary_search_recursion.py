def search(arr, target, start, end):

	if (end >= start):	
		mid = (start + end) // 2

		if (arr[mid] > target):
			search(arr,target, start, mid-1)
		elif (arr[mid] < target):
			search(arr,target, mid+1, end)
		else:
			print(mid)
	else:
		print("not found")

arr = [2, 4, 8, 9, 12, 15, 18, 41, 81]
target = 81
