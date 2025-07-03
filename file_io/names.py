with open('names.txt', 'a') as file:
    name = input("What's your name? ")
    file.write(f'{name}\n')