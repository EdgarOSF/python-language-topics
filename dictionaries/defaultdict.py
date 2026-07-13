import collections

# Un defaultdict nos ayuda para trabajar con 
# las missing keys, asi que cuando aun defaultdict
# si le pasamos una key que no contiene el diccionario
# internamente creara una nuevo objeto, con la nueva key del tipo que
# le pasamos en el constructor.

my_dict = collections.defaultdict(dict)

print(my_dict['name'])
