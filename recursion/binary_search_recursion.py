def search(arr, target, start, end):

	if (end >= start):	
		mid = (start + end) // 2

		if (arr[mid] > target):
			search(arr,target, start, mid-1)
		elif (arr[mid] < target):
			search(arr,target, mid+1, end)
		else:
			return mid
	else:
		return -1