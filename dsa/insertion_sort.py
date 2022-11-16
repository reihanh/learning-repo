def sort(arr):
	iteration = 0

	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1

		while j >= 0 and arr[j] > key:
			iteration += 1

			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key

	return arr, iteration


arr = [9,8,7,6,5,4,3,2,1]

print(sort(arr))