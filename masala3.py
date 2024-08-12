myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

myDct = dict(map(lambda x: (x, myList.count(x)), set(myList)))

print(myDct)