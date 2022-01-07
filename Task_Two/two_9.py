x = 0

is_continue="yes"

while is_continue == "yes":

    x = input("Enter the lucky number or type no to exit : ")

    if x == 'no':
        break
    elif int(x) == 6:
        print("you guessed the correct number")
        is_continue = "no"
        break
    else:
        continue