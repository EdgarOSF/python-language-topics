users = ['edgaro', 'dennise', 'admin', 'jpepe']


def hello_admin(users: list):

    if users:
        for user in users:
            if user == 'admin':
                print(f'Hello {user}, would you like a status report?')
            else:
                print(f'Hello {user}, thank you for logging in again.')
    else:
        print('We need to find some users!')


hello_admin([])
hello_admin(users)