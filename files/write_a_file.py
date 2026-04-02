print('Create a file in write mode')
f = open('data.txt', 'w')
print('Writes text in the file')
print(f.write('Hello\n'))

print(f.write('Hello!\n'))
f.close()
