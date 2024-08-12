def array(arr):
    birinchi = next(filter(lambda x: x % 2 == 0, arr), None)
    return list(map(lambda x: x + birinchi if x % 2 == 0 else x, arr)) if birinchi is not None else arr

arr = [1, 3, 4, 7, 8]
result = array(arr)
print(result)
