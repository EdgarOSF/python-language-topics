import itertools


my_list = [1,2,3]

permutations = itertools.permutations(my_list)
permutations2= list(itertools.permutations(my_list))

print(permutations)
print(permutations2)