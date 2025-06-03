import re


mo = re.compile(r'Batman|Tyna Fey')
mo1 = mo.search('Batman y Tyna Fey')

# print(mo1.group())

batRegex = re.compile(r'Bati(movil|cueva|bumerang|cinturon)')
bat1 = batRegex.search('La Baticueva esta escondida')

# print(bat1.group())
# print(bat1.group(1))


# Coincidencia opcional con el signo de interrogacion
# coincide con cero o una instancia de wo
batRegex1 = re.compile(r'Bat(wo)?man')
bat2 = batRegex1.search('Las aventuras de Batwoman')

# print(bat2.group())
# print(bat2.group(1))

# Numero de telefono que tenga o no codigo de area
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo2 = phoneRegex.search('Mi numero es 993-194-8106')
mo3 = phoneRegex.search('Mi numero es 194-8106')

# print('Numero con codigo', mo2.group())
# print('Numero sin codigo', mo3.group())

# Coincidiento con cero o mas con *
# el grupo que preceda al * puede aparecer cualquier cantidad de veces
# Puede estan completamente ausente o repetirse una y otra vez
batRegex2 = re.compile(r'Bat(wo)*man')
mo4 = batRegex2.search('Las aventuras de Batman')
# print(mo4.group())
mo5 = batRegex2.search(r'Las aventuras de Batwoman')
# print(mo5.group())
mo6 = batRegex2.search('Las aventuras de Batwowowowowowoman')
# print(mo6.group())
# print(mo6.group(1))


# Coincidir con uno o mas con el signo mas.
# Significa "Coincidir con uno o más".
batRegex3 = re.compile(r'Bat(wo)+man')
mo7 = batRegex3.search('Las aventuras de Batman')
mo8 = batRegex3.search(r'Las aventuras de Batwoman')
mo9 = batRegex3.search('Las aventuras de Batwowowowowowoman')
# print(mo8.group())
# print(mo9.group())
# print(mo7 == None)

# Cooincidencia de repeticiones especificas con llaves
'''Si tiene un grupo que desea repetir una cantidad específica de veces, coloque un 
número entre llaves después del grupo en su expresión regular. Por ejemplo, 
la expresión regular (Ha){3} coincidirá con la cadena 'HaHaHa' ,pero no con 'HaHa' , 
ya que esta última solo tiene dos repeticiones del grupo (Ha) .
En lugar de un número, puedes especificar un rango escribiendo un mínimo, una coma y un máximo entre llaves. 
Por ejemplo, la expresión regular (Ha){3,5} coincidirá con 'HaHaHa' , 'HaHaHaHa' y 'HaHaHaHaHa' .
También puede omitir el primer o segundo número entre llaves para dejar el mínimo o máximo sin acotar. 
Por ejemplo, (Ha){3,} coincidirá con tres o más instancias del grupo (Ha) , mientras que (Ha){,5} coincidirá con cero a cinco instancias. '''
haRegex = re.compile(r'(Ha){3}')
mo10 = haRegex.search('HaHaHa')
mo11 = haRegex.search('HaHa')
# print(mo10.group())
# print(mo11 == None)

haRegex2 = re.compile(r'(Ha){3,5}')
mo12 = haRegex2.search('HaHaHaHaHa')
mo13 = haRegex2.search('HaHaHa')
mo14 = haRegex2.search('HaHaHa')
# print(mo12.group())
# print(mo13.group())
# print(mo14 == None)

'''Las expresiones regulares de Python son voraces de forma predeterminada, lo que significa que en situaciones 
ambiguas coincidirán con la cadena más larga posible. La versión no voraz (también llamada lazy ) de las llaves, 
que coincide con la cadena más corta posible, tiene la llave de cierre seguida de un signo de interrogación.
Tenga en cuenta que el signo de interrogación puede tener dos significados en las expresiones regulares: 
declarar una coincidencia no codiciosa o marcar un grupo opcional. Estos significados no tienen ninguna relación.'''
haRegex3 = re.compile(r'(Ha){3,5}?')
# mo15 = haRegex3.search('HaHaHaHaHa')
# print(mo15.group())


# Metodo findall()
'''Además del método search() , los objetos Regex también tienen un método findall() . Mientras que search() devolverá un 
objeto Match del primer texto coincidente en la cadena buscada, el método findall() devolverá las cadenas de cada Coincidencia en la cadena buscada.
Por otro lado, findall() no devolverá un objeto Match sino una lista de cadenas, siempre que no haya grupos en la expresión regular .'''
phoneRegex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
'''Si hay grupos en la expresión regular, findall() devolverá una lista de tuplas. Cada tupla representa una coincidencia encontrada y sus elementos 
son las cadenas coincidentes para cada grupo en la expresión regular. '''
phoneRegex3 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# print(phoneRegex2.findall('Celular: 415-555-9999 Trabajo: 212-555-0000'))
# print(phoneRegex3.findall('Celular: 415-555-9999 Trabajo: 212-555-0000'))

# Clases de caracteres
'''Shorthand character class        Represents
    \\d                              Any numeric digit from 0 to 9.
    \\D                              Any character that is not a numeric digit from 0 to 9.
    \\w                              Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
    \\W                              Any character that is not a letter, numeric digit, or the underscore character.
    \\s                              Any space, tab, or newline character. (Think of this as matching “space” characters.)
    \\S                              Any character that is not a space, tab, or newline.'''
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
