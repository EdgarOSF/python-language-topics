from collections import defaultdict


# Un defaultdict asigan un valor por default a una key inexistente
# Devuelve un tipo de dict
# Cuando se llama a una key inexistente defaultdict llama a la fabrica, almacena el resultado y lo devuleve.
# Este comportamiento diferencia a defaultdict del metodo get()

puestos = defaultdict()

puestos["backend"] = "edgar"
puestos["frontend"] = "carlos"
puestos["database"] = "davis"
puestos["backend"] = "omar"

print(puestos)

print()

puestos2 = defaultdict(list)
puestos2["backend"].append("edgar")
puestos2["frontend"].append("carlos")
puestos2["database"].append("davis")
puestos2["backend"].append("omar")

print(puestos2.items())
print(sorted(puestos2.items()))

print()

s = [("yellow", 1), ("blue", 2), ("yellow", 3), ("blue", 4), ("red", 1)]
dd = defaultdict(list)

for k, v in s:
    dd[k].append(v)

print(sorted(dd.items()))

print()

## defaultdict para agrupaciones
print("defultdict para Agrupaciones")
inscripciones_por_grupo = defaultdict(list)
lista_normal = dict()

inscripciones = [
    ("A", "Edgar omar"),
    ("B", "Carlos Espino"),
    ("A", "Matt Fraser"),
]

for grupo, alumno in inscripciones:
    inscripciones_por_grupo[grupo].append(alumno)

print(inscripciones_por_grupo)

# for grupo, alumno in inscripciones:
#     lista_normal[grupo].add(alumno)

print(lista_normal)

print()

# Agrupacion sin duplicados
print("Agrupacion sin duplicados")

permisos = defaultdict(set)

permisos["edgar"].add("lectura")
permisos["edgar"].add("escritura")
permisos["edgar"].add("lectura")

print(permisos["edgar"])

print()

# Acumulacion, aun que para esta operacion es mejor Counter.
print("Acumulacion")

totales = defaultdict(int)

ventas = [
    ("laptop", 10_000),
    ("mouse", 1_000),
    ("laptop", 15_000),
]

for articulo, precio in ventas:
    totales[articulo] += precio

print(totales)

print()

# Diccionarios anidados
print("Diccionarios anidados")

calificaciones = defaultdict(lambda: defaultdict(list))

calificaciones["Python"]["Unidad 1"].append(90)
calificaciones["Python"]["Unidad 1"].append(85)
calificaciones["Java"]["Unidad 1"].append(95)

print(calificaciones)

print()

print("get() no llama a default factory")

datos = defaultdict(list)

print("con get ->", datos.get("inexistente"))
print('con datos["inexistente"] ->', datos["inexistente"])
