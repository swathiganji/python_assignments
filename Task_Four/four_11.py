
lst = [i for i in range(1, 11)]
lst1 = list(filter(lambda x : x % 2 == 0, lst))
lst2 = list(map(lambda x : x*2, lst1))
print(lst2)