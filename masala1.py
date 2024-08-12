lst = ["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"]
n = int(input("masofani kiriting: "))

result = list(map(lambda ajrat: lst[ajrat:ajrat + n], range(0, len(lst), n)))

print(result)
