current_users = ['jose', 'edgar', 'OMAR', 'eduardo']
current_users_lower = [username.lower() for username in current_users]
new_users = ['carlos', 'carmen', 'jose', 'pepe', 'omar']

for new_user in new_users:
    if new_user in current_users_lower:
        print(f'Sorry {new_user}, will need to enter a new username.')
    else:
        print(f'The username {new_user} is avaliable.')