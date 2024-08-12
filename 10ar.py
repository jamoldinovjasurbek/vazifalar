arr = [1, 2, 3, 4, 5, 6, 7]
k, h = 2, 5

arr = arr[:k] + arr[k+1:h-1] + [arr[k]] + arr[h-1:k:-1] + arr[h:]

print(arr)
