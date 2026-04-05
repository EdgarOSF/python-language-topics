import json

# Serilize object python to json
dog_registry = {1: {"name": "Laica"}}

dog_json = json.dumps(dog_registry)

print("Python Object:")
print(dog_registry)

print("Json Object")
print(dog_json)

print()

print("Complex Example")

dog_registry = {
    1: {
        "name": "Laica",
        "is_dog": True,
        "hobbies": ["eating", "sleeping", "barking"],
        "age": 15,
        "address": {
            "work": None,
            "home": ("Tabasco", "Mexico")
        },
    }
}

print(dog_registry)

print()

dog_json = json.dumps(dog_registry)

print(dog_json)

print()

dog_new_data = json.loads(dog_json)
print(dog_new_data)

print()

print(dog_registry == dog_new_data)







