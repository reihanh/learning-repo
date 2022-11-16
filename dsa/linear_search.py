def search(arr, target):
	for i in range(len(arr)):
		if arr[i] == target:
			return i
	return -1

arr = [4,9,12,15,2,8,18,41,81]
target = 81

print(search(arr,target))