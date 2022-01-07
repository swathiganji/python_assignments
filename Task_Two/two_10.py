y = 0
while y <= 5:
    if y == 5:
        print("Game Over!")
        break
    x = int(input("Enter your number: "))
    if x == 60:
        print("Good Guess")
        y += 1
        continue
    else:
        print("Try Again!")
        y += 1
        continue