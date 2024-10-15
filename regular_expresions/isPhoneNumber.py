import re


phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegexEscape = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search('Mi numero es 993-194-8106')
moe = phoneNumRegexEscape.search('Mi numero es (993) 194-8106')
codArea, numPrincipal = mo.groups()

print('Numero de telefono encontrado:', mo.group())

print('Codigo de area:', mo.group(1))
print('Numero principal:', mo.group(2))
print('Todos los grupos:', mo.group(0))
print('Todos los grupos:', mo.group(0))
print('Todos los grupos:', codArea)
print('Todos los grupos:', numPrincipal)
print('Regex con escape de caracteres:', moe.group())


# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
    
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
        
#     if text[3] != '-':
#         return False
    
#     for i in range(4, 7):
#         if not text[i].isdecimal():
#                 return False
        
#     if text[7] != '-':
#         return False
    
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#                 return False
        
    

    # return True

# print('Is 415-555-4242 a phone number?')
# print(isPhoneNumber('415-555-4242'))
# print('Is Moshi moshi a phone number?')
# print(isPhoneNumber('Moshi moshi'))

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')