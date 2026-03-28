print('In function calls, we can use * multiple times')
def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*[1, 2], 3, *range(4, 7)))

print('More explamples...')
print(*range(4), 4)
print([*range(4), 4])
print({*range(4), 4, *[5, 6, 7]})