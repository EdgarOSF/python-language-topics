from collections import Counter
from math import prod

# Factores primos del numero 1836

factores = Counter({2: 2, 3: 3, 17: 1})
producto = 1


for f in factores.elements():
    producto *= f

# otra forma de obtener el mismo resultado es usando math.prod
math_prod = prod(factores.elements())


print(producto)
print(f"producto con math.prod(): {math_prod}")
