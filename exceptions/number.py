# Version 1 
# try:
#     number = int(input("What's x: "))

#     print(f'X is {number}')

# except ValueError:
#     print('X is not an integer')

# Version 2
# while True:
#     try:
#         x = int(input("What's x: "))
#     except ValueError:
#         print('X is not an integer')
#     else:
#         break

# print(f'X is {x}')

# Version 3
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x: "))
#         except ValueError:
#             print('X is not an number')
#         else:
#             return x # Aqui return tanto sale del blucle, tambien retorna el valor de x.

# Version 4
def get_int():
    while True:
        try:
            return int(input("What's x: "))
        except ValueError:
            print('X is not an number')

def main():
    x = get_int()
    print(f'X is {x}')

main()