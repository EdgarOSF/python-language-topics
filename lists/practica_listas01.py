invitados = [
    'Erika Lissete Reyes Morales',
    'Edgar Fernando Rosique Arias',
    'Jorge Alfredo Perez Ruiz',
    'Adrian Cortes Solano',
    'Dennis Emir Sanchez Farias',
    'Mayanini del R. Farias Reyes',
    ]

print('##### LISTA DE INVITADOS #####')
for invitado in invitados:
    print(f'{invitado}, estas invitado a una cena conmigo.')

remplazo = 'Jose Manuel Ble Lanestosa'

print(f'\n{invitados[3]} no podrà asistir a la cena y sera remplazado por {remplazo}.\n')

invitados[3] = remplazo

print(f'Asi queda la nueva lista de invitados {invitados}\n')