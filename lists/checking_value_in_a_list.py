names = ['edgar', 'omar', 'Dennis', 'emir']

print('edgar' in names)
print('dennis' in names)
print('Dennis' in names)

menu = ['pizza', 'hamburger', 'seafood']
food = 'salad'
if food not in menu:
    print(f'{food.title()} is not in the menu, today.')