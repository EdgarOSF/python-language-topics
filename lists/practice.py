# Counting to twenty
# for number in range(1, 21):
#     print(number)

# Suma los numeros de 1 a 1 000 0000
# one_million = [ number for number in range(1, 1000001)]
# print('Número minimo', min(one_million))
# print('Número máximo', max(one_million))
# print(sum(one_million))

# Odd numbers from 1 to 20
# odd = [ number for number in range(1, 20, 3)]
# print(odd)

# Cube of each number from 1 to 10
cubes = list(range(1, 10))
for number in cubes:
    print(number**3)

# Cube of each number from 1 to 10 with list comprehension
cubes_lc = [ number ** 3 for number in range(1, 10)]
print(cubes_lc)