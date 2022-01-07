
def shownumbers(limit):
    for i in range(limit+1):
        if i == 0:
            print(i, "EVEN")
        elif i%2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")
shownumbers(3)
