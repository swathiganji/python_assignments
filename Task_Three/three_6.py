

lst = [i for i in range(1,31)]
lst_new = lst[:5] + lst[-5:]

lst_squared = [i**2 for i in lst_new]

print(lst_squared)