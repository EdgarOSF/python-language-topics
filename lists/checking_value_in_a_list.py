# names = ['edgar', 'omar', 'Dennis', 'emir']

# print('edgar' in names)
# print('dennis' in names)
# print('Dennis' in names)

# menu = ['pizza', 'hamburger', 'seafood']
# food = 'salad'
# if food not in menu:
#     print(f'{food.title()} is not in the menu, today.')

# Usando multiples listas

ingredientes_disponibles = ['champiñones', 'cebolla', 'tomate', 'carne_molida', 'peperoni']

ingredientes_solicitados = ['champiñones', 'aceitunas', 'tomate', 'peperoni']


for ingrediente_solicitado in ingredientes_solicitados:
    if ingrediente_solicitado in ingredientes_disponibles:
        print(f'Agregando {ingrediente_solicitado}.')
    else:
        print(f'Lo sentimos, no tenemos {ingrediente_solicitado}')

print('Terminamos de preparar tu pizza!')