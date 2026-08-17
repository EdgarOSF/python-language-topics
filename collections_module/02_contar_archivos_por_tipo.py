from collections import Counter
from pathlib import Path


entradas = Path("C:/Users/Edgar Omar/Downloads/").iterdir()

extensiones = [item.suffix for item in entradas if item.is_file()]

print(Counter(extensiones))

