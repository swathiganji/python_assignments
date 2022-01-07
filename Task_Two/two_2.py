

x = int(input("Enter 1 for additon, enter 2 for subtraction, enter 3 for Division, enter 4 for Multiplication, enter 5 for Avarage : "))
if x == 1:
    a = int(input("enter a number: "))
    b = int(input("Enter a number: "))
    c = a + b
    if c >= 0:
        print(c)
    else:
        print("NEGATIVE")


if x == 2:
    a = int(input("enter a number: "))
    b = int(input("Enter a number: "))
    c = a - b
    if c >= 0:
        print(c)
    else:
        print("NEGATIVE")


if x == 3:
    a = int(input("enter a number: "))
    b = int(input("Enter a number: "))
    c = a / b
    if c >= 0:
        print(c)
    else:
        print("NEGATIVE")

if x == 4:
    a = int(input("enter a number: "))
    b = int(input("Enter a number: "))
    c = a * b
    if c >= 0:
        print(c)
    else:
        print("NEGATIVE")
if x == 5:
    a = int(input("enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    d = int(input("Enter a number: "))
    z = a + b + c + d
    avg = z/4
    if avg >= 0:
        print(avg)
    else:
        print("NEGATIVE")