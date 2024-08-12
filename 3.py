def array(arr):
    last_odd = next(filter(lambda x: x % 2 != 0, arr[::-1]), None)
    return list(map(lambda x: x + last_odd if x % 2 != 0 else x, arr)) if last_odd is not None else arr
arr = [2, 3, 4, 6, 7]
result = array(arr)
print(result)
