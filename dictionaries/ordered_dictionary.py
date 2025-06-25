favorite_languages = {
    'edgar': 'python',
    'eduardo': 'python',
    'iran': 'python',
    'omar': 'java',
    'carlos': 'c#',
    'fernando': '.Net',
    'jose': 'javascript',
    'jorge': 'rust',
}


for name in sorted(favorite_languages.keys()):
    print(name.title())

for languaje in sorted(favorite_languages.values()):
    print(languaje.title())

for languaje in set(favorite_languages.values()):
    print(languaje)