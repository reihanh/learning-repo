def search(arr, target):
	start = 0
	end = len(arr)-1

	while start <= end:	
		mid = (start + end) // 2
		print(mid)

		if (arr[mid] > target):
			end = mid - 1
		elif (arr[mid] < target):
			start = mid + 1
		else:
			return f"This on position {mid}"

arr = [2, 4, 8, 9, 12, 15, 18, 41, 81]
target = 41

print(search(arr,target))

# note
# array must be sorted first, so if array is unsorted then sort first