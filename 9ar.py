arr = [1, 2, 3, 4, 5, 6]

min = arr.index(min(arr))
max = arr.index(max(arr))
if min > max:
    min, max = max, min

arr = arr[:min+1] + list(map(lambda l: 0, arr[min+1:max])) + arr[max:]

print(arr)
