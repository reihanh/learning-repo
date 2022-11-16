# array must be sorted first, so if array is unsorted then sort first

def search(arr, target):
	start = 0
	end = len(arr)-1

	while start <= end:	
		mid = (start + end) // 2

		if (arr[mid] > target):
			end = mid - 1
		elif (arr[mid] < target):
			start = mid + 1
		else:
			return mid