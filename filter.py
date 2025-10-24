numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(n):
    return n % 2 == 0

result = list(filter(is_even, numbers))

print(result)