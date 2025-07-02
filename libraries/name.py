import sys

# Version 1
# if len(sys.argv) < 2:
#     print('Too few arguments')
# elif len(sys.argv) > 2:
#     print('Too many arguments')
# else:
#     print(f'Hello my name is {sys.argv[1]}')

# Version 2
# if len(sys.argv) < 2:
#     sys.exit('Too few arguments')
# elif len(sys.argv) > 2:
#     sys.exit('Too many arguments')

# print(f'Hello my name is {sys.argv[1]}')

# Version 3
if len(sys.argv) < 2:
    sys.exit('Too few arguments')

for name in sys.argv[1:]:
    print(f'Hello my name is {name}')