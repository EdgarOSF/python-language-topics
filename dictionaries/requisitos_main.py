from requisitos import data


for row in data:
    print(row['documento'].upper())
    if row['requisitos']:
        for documentacion in row['requisitos']:
            requisito = documentacion['requisito'][11:].strip().title()
            cargado = "✅" if documentacion['documento_requisito'] else "✖️"
            print(f"\t- {requisito}: {cargado}")
    else:
        print("\tSin requisitos.")
