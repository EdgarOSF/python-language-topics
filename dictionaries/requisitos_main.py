from requisitos import data


for row in data:
    for _, documento in row.items():
        print(documento)
        # if requisitos:
        #     for row_requisitos in requisitos:
        #         print(f"\tRequisito: {row_requisitos['requisito']}")
        #         print(f"\tDocumento: {row_requisitos['documento_requisito']}")
        # else:
        #     print('Este documento no tiene requisitos.')