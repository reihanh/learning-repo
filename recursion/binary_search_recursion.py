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

arr = [2, 4, 8, 9, 12, 15, 18, 41, 81]
target = 7

result = search(arr,target, 0, len(arr)-1)

if result != -1:
	print(f"element on index {result}")
else:
	print("element not found")