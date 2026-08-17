from collections import Counter
import re

# \w+ = uno o mas caracteres de la "a" a la "Z", incluyendo los digitos del 0-9 y el "_"
# read() = lee todo el tesxto como si fuera una unica linea.

palabras = re.findall(r"\w+", open("./hamlet.txt").read())

print(Counter(palabras).most_common(10))

# Resultado: [('the', 930), ('and', 695), ('to', 638), ('of', 630), ('I', 610), ('you', 483),
# ('a', 478), ('my', 444), ('in', 412), ('it', 359)]
