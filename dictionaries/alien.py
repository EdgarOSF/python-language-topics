alien_0 = { 'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(alien_0['x_position'])


# Remove key-pair value
del alien_0['points']

print(alien_0)

# print(alien_0['points'])

# get value using get
print(alien_0.get('points', 'No point value asigned.'))