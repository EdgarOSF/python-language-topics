favorite_languages = {
    'jan': ['Python', 'Rust'],
    'peter': ['Python'],
    'phill': ['Javascript', 'Css'],
    'sarah': ['C'],
    'eduard': ['Rust', 'Go'],
}


for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
    else:
        print(f"{name.title()}'s favorite language is:")
    
    for language in languages:
        print(f'\t{language}')