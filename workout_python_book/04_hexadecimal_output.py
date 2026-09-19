def hex_output(hex_num):
    dec_num = 0

    for power, digit in enumerate(reversed(hex_num)):
        try:
            dec_num += int(digit, 16) * (16**power)
        except ValueError as e:
            return e

    return dec_num


print(hex_output('123'))
print(hex_output('ff'))

