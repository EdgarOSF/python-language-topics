names = []

# Version 1
# with open('names.txt') as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(name)

# version 2 more compact

with open('names.txt') as file:
    for line in sorted(file):
        print(f'Hello {line.rstrip()}')