coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]
result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v = zip(*resultList)
print('\nc =', c)
print('\nv =', v)