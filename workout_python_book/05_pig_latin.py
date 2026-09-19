import string


def pig_latin(str_input):
    clean_input = str_input.strip().lower()
    str_output = clean_input

    if not clean_input:
        raise ValueError('Please enter a word')

    if str_input[-1] in string.punctuation:
        suffix = str_input[-1]
        str_output = str_input.removesuffix(suffix)
    
    if clean_input[0] in 'aeiou':
        str_output = f'{str_output}way'
    else:
        str_output = f'{str_output[1:]}{str_output[0]}ay'
    
    if str_input.istitle():
        str_output = str_output.title()
    if str_input[-1] in string.punctuation:
        str_output = f'{str_output}{suffix}'
    return str_output

def pig_latin_alt(str_input):
    clean_input = str_input.strip().lower()

    if not str_input:
        raise ValueError('Please enter a word')

    vowels_in_word = set(clean_input) & set('aeiou')

    if len(vowels_in_word) == 1:
        return f'{clean_input[1:]}{clean_input[0]}ay'
    elif len(vowels_in_word) > 1:    
        return f'{clean_input}way'
    return pig_latin(str_input)



# print(pig_latin('')) # ValueError
print(pig_latin('air'))
print(pig_latin('eat'))
print(pig_latin('Eat'))
print(pig_latin('Air'))
print(pig_latin('python'))
print(pig_latin('computer'))
print(pig_latin('python.'))
print(pig_latin('python!'))
print(pig_latin('Python?'))
print(pig_latin_alt('wine'))
print(pig_latin_alt('wind'))


