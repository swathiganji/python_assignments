
def maxlen():
    str1 = input("Enter your first word: ")
    str2 = input("Enter your second word: ")
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) == len(str2):
        print("the strings are line by line")
    else:
        print(str2)
maxlen()