

x = input("enter hyphen-separated sequence of words: ")
xl = x.split('-')
xl.sort()
xj = "-".join(xl)
print(xj)
