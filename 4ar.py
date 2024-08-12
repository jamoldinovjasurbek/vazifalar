arr = [3, 1, 5, 7, 2]

min = arr.index(min(arr))
max = arr.index(max(arr))
arr[min], arr[max] = arr[max], arr[min]

print(arr)
