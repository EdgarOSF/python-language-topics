# Create a file in read mode(default)
f = open('data.txt')
text = f.read()
print(text)

print(text.split())

# Display lines in a file
f2 = open('data.txt', 'w')
f2.write('Hello\nWorld!\n')
f2.write('GoodBye\n')

for line in open('data.txt'):
    print(line.rstrip())
