responses = {}

polling_active = True

while polling_active:

    name = input("What's your name? ")
    response = input('Which mountain would you like to climb someday? ')

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == 'no':
        polling_active = False

for name, r in responses.items():
    print(f'{name}: {r}')

    