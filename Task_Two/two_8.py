x = input("Enter a word: ")
i = 0
y = 0
for ch in x:
    if ch.isalpha():
        i += 1
        continue
    else:
        y += 1
        continue
print("Letters = ",i)
print("Digits = ", y)
