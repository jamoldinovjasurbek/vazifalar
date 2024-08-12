def array(arr, k):
    return list(map(lambda x: x + arr[k-1], arr))
arr = [1, 2, 3, 4, 5]

k = 3
result = array(arr, k)

print(result)
