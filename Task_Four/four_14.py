def divisible_by_7_not_3(x):
    if x % 3 == 0:
        return False
    elif x % 7 == 0:
        return True
    else:
        return False


for i in range(1, 100):
    if divisible_by_7_not_3(i):
        print(i)
