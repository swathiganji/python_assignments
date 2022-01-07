
a = 10
b = 20
c = 30
z = a+b+c
avg = z/3
print("avarage: ",avg)
if avg > a and avg>b and avg>c:
    print("avg is higher than a, b, c")
elif avg>a and avg>b:
    print("avg is higher than a, b")
elif avg>a and avg>c:
    print("avg is higher than a, c")
elif avg>b and avg>c:
    print("avg is higher than b, c")
elif avg>a:
    print("avg is just higher than a")
elif avg>b:
    print("avg is just higher than b")
elif avg>c:
    print("avg is just higher than c")
