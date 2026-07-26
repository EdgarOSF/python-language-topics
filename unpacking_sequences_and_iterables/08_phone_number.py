phones = ["9931948106", "7717025030"]
for phone in phones:
    match tuple(phone):
        case ["99", *rest]:
            print("Tabasco")
        case "55", *rest:
            print("CDMX")
        case "77", *rest:
            print("Pachuca")
