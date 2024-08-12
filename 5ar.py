arr = [1, 2, 3, 4, 5, 6]

arr = list(map(lambda i: arr[i+1] if i % 2 == 0 else arr[i-1], range(len(arr))))

print(arr)
