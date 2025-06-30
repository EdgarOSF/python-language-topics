from requisitos import data


for row in data:
    print(row['documento'])
    print(f"\t{row['requisitos']}")