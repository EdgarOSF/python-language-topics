import os
from pathlib import Path

# imprime el directorio actual
# print(Path.cwd())

# Imprime los archivos del directorio actual
# for i in Path().iterdir():
# print(i)

# imprime un archivo en particular
# print(Path("dictionaries.py"))

my_dir = Path("clases")
my_file = Path("equipo_limpieza.py")

print(my_dir)
print(my_file)

print(my_dir.name)
print(my_file.name)

print()

# imprimir la extension de un archivo
print(my_file.suffix)

# imprimir el nombre del archivo
print(my_file.stem)

print()

# creacion de rutas
# forma 1
my_new_file = my_dir / "new_text.txt"
print(my_new_file)
# forma 2
my_new_file_2 = my_dir.joinpath("other_file.txt")
print(my_new_file_2)

print()

# Verificar la existensia de rutas y archivos
print(my_dir.exists())
print(my_file.exists())
print(my_new_file.exists())
print(my_new_file_2.exists())

print()

# saber el directorio padre
print(my_dir.parent)
print(my_file.parent)
print(my_new_file.parent)
print(my_new_file.parent.parent)

print()

# rutas absolutas
print(my_new_file.absolute())
print(my_new_file.resolve())
