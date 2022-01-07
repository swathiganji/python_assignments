def example():
    x = input("Enter a word: ")
    u = 0
    l = 0
    for i in x:
        if i == i.upper():
            u += 1
        elif i == i.lower():
            l += 1

    print("No. of Uppercase characters: ",u , "No. of Lower case Characters: ", l)
example()

