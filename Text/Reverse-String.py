string = input('Enter the string\n')
newStringList = []
for char in string:
    newStringList.insert(0, char)

print(''.join(newStringList))

