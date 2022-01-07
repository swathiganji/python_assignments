
from functools import reduce
lst = [1, 2, 3, 4, 5, 6, 7]
lst1 = reduce(lambda x, y:10*x+y,lst )
print(lst1)

lst2 = reduce(lambda x,y: x+y,['1','2','3','4','5','6','7'])
print(lst2)