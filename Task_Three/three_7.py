

lst = [1,3,5,7,9,10]
lst1 = lst[:-1]
lst2 = [2, 4, 6, 8]
lst3 = lst1 + lst2
print(lst3)

lst = [1,3,5,7,9,10]
lst1 = lst[:-1]
lst2 = [2, 4, 6, 8]
lst1.extend(lst2)
print(lst1)
