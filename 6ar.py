arr = [1, 2, 3, 4, 5, 6]

mid = len(arr) // 2
arr = arr[mid:] + arr[:mid]

print(arr)
