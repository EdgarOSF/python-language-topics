from collections import ChainMap


# un chainmap retiene una lista de objos mapping que pueden ser buscados como uno.
# un chainmap no hace una copia de los mappings pero si una referencia.
# los Update o insertions solo afectan al primer mapping de entrada.
# Si uno de los mapeos de un chainmap se actualiza, se reflejaran en el chainmap.

l1 = dict(a=1, b=2)
l2 = dict(c=3, d=4)
chain = ChainMap(l1, l2)
print(chain)
print(chain["a"])
print(chain["d"])
print("Modificacion")
chain["d"] = -4
print(chain)  # ChainMap({'a': 1, 'b': 2, 'd': -4}, {'c': 3, 'd': 4})


import builtins

pylockups = ChainMap(locals(), globals(), vars(builtins))
print(pylockups)

