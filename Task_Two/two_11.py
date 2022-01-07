y = 0
while y <= 5:
    if y == 5:
        print("Sorry but that was not very successful")
        break
    x = int(input("Enter your number: "))
    if x == 60:
        print("Good Guess")
        break
    else:
        print("Try Again!")
        y += 1
        continue
