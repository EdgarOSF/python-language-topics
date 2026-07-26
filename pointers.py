dict1 = {"number": 11}
dict2 = dict1

print("dict1:", id(dict1), dict1)
print("dict2:", id(dict2), dict2)

dict2["number"] = 22

print("\ndict1:", id(dict1), dict1)
print("dict2:", id(dict2), dict2)

dict3 = {"number": 33}
dict2 = dict3
print("\ndict3:", id(dict3), dict3)
print("dict2:", id(dict2), dict2)

dict1 = dict3
print("\ndict3:", id(dict3), dict3)
print("dict2:", id(dict2), dict2)
print("dict1:", id(dict1), dict1)
