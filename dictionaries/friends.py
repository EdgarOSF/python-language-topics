favorite_languages = {
    'edgar': 'python',
    'omar': 'Java',
    'carlos': 'C#',
    'fernando': '.Net',
    'jose': 'Javascript',
    'jorge': 'Rust',
}


friends = ['omar', 'jose']

for name in favorite_languages.keys():
    print(f'Hi {name.title()}')

    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, i see you love {language}')

if 'erin' not in favorite_languages.keys():
    print(f'Erin please take our poll!')