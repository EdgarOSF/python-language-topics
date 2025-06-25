aliens = []

for alien_number in range(30):
    new_alien = { 'color': 'green', 'points': 5, 'speed': 'low'}
    aliens.append(new_alien)


print(f'Total number of aliens {len(aliens)}')


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 8
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '12'
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)