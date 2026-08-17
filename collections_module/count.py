from collections import Counter
import collections

"""Counter es una subclase de Dict"""


palabra = ["abracadabra"]

print(
    collections.Counter("abracadabra")
)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

lenguajes = ["python", "java", "python", "c++", ".net", "java", "java"]

conteo = collections.Counter(lenguajes)

print(
    collections.Counter(lenguajes)
)  # Counter({'java': 3, 'python': 2, 'c++': 1, '.net': 1})

print(f"Python: {conteo['python']}")
print(f"Java: {conteo['java']}")

print()

# Counter devuelve 0 si no encuentra un indice
print(f"Clave inexistente devuelve 0: {conteo['dart']}")


print()

vacio = Counter()
print(vacio)

print()

desde_iterable = Counter("missisipi")
print(desde_iterable)

print()

desde_diccionario = Counter({"activo": 10, "inactivo": 15})
print(desde_diccionario)

print()

desde_argumentos = Counter(aprovado=10, reprovado=4)
print(desde_argumentos)
print(type(desde_argumentos))

print()

#### Metodos importantes ####

## most_common()
lenguajes_counter = Counter(["python", "java", "python", "c++", ".net", "java", "java"])
print(lenguajes_counter.most_common())

print()

# Metodo update()
# argumentos
# Aumenta el contador, no lo reemplaza con el metodo update de dict.
desde_argumentos.update(repite=2)
print(desde_argumentos)

print()

## elements() : Retorna los elementos el numero de veces igual a su contador,
## e ignora los elementos menores de 1.
# Devuelve  un iterable repitiendo cada elemento las veces de su conteo
print("Metodo elements()")
c = Counter("misissipi")
c2 = Counter("aabbbbcccccd")
c3 = Counter(a=2, b=2, c=-1)
print(sorted(Counter(c).elements()))
print(sorted((c2).elements()))
print(list(c3.elements()))
print("".join(c.elements()))

print()

## subtract() : Se restan los elementos de un iterable o de otro mapeo.
print("Metodo subtract()")
ca = Counter(a=3, b=4, c=5)
cb = Counter(a=1, b=2, c=4)
ca.subtract(cb)
print(ca)
print("otro ejemplo con subtract()")
inventario = Counter(laptop=10, monitor=8, teclados=5)
ventas = Counter(laptop=5, monitor=8, teclados=7)
inventario.subtract(ventas)
print(inventario)

print()

## total() : Computa las sumas de los contador
print("Metodo total()")
cc = Counter(pizza=12, vasos=4, platos=4)
print(cc)
print(cc.total())

print()

# Operaciones matematicas que permiten combinar objetos Counter
print("Operacione matematicas con objetos Counter")
cc = Counter(a=3, b=1, c=0, d=-4)
cc2 = Counter(a=1, b=4)
print(f"operacion +: {cc} + {cc2} = {cc + cc2}")
print(f"operacion - (solo valores positivos): {cc} - {cc2} = {cc - cc2}")
print(
    f"operacion interseccion(&) (retornara el minimo de cada objeto): {cc} & {cc2} = {cc & cc2}"
)
print(f"operacion union(|) (valores maximos): {cc} | {cc2} = {cc | cc2}")
print(f"operacion igual(==): {cc} = {cc2} == {cc == cc2}")
print(f"operacion inclusion (<=): {cc} <= {cc2} = {cc <= cc2}")
print(f"operacion suma unaria (Devuelve los valores mayores a 0): +{cc} = {+cc}")
print(f"operacion resta unaria (Devuelve los valores menores a 0): -{cc} = {-cc}")
