def mysum(*numbers):
    output = 0

    for number in numbers:
        output += number

    return output


print(mysum(10, 20, 30, 40)) # 100


def average(numbers):
    if not numbers:
        raise ValueError('Parameters are empty')

    list_numbers = list(numbers)

    acc = 0
    len_list = len(list_numbers)

    for number in list_numbers:
        acc += number

    return acc / len_list


print(average([10, 20, 30, 40])) # 25.0
# print(average([])) # ValueError: Parameters is empty


def list_of_words(words):
    if not words:
        raise ValueError('The list is empty')

    list_words = list(words)

    words_len = [len(word) for word in list_words]

    output = (min(words_len), max(words_len), average(words_len))

    return output


print(list_of_words(['hola', 'omar', 'dennis', 'eduardo', 'otorrinolaringologia', 'programacion', 'python', 'java', 'hola', 'python', 'java']))
try:
    print(list_of_words([])) # ValueError
except ValueError:
    pass
