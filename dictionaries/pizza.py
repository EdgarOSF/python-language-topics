pizza = {
    'crust': 'thick',
    'toppings': ['peperoni', 'cheese', 'pepper']
}


print(f'You ordereda pizza {pizza["crust"]}-crust pizza with the following toppings:')

for toppping in pizza['toppings']:
    print(f'\ttoppping')

