arr = [1, 2, 3, 4, 5, 6]

minimal, maximal = arr.index(min(arr)), arr.index(max(arr))
arr[minimal], arr[maximal] = arr[maximal], arr[minimal]

print(arr)
