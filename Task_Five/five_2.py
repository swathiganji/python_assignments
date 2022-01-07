import sys
filename = sys.argv[]
file = open(filename, 'r')
lines = file.readlines()
for line in lines:
    print(line)