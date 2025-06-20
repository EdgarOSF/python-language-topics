fecha = '07:05:45PM'
fecha2 = '12:01:45AM'
fecha3 = '11:01:45AM'
fecha4 = '12:45:54PM'

def timeConversion(s):

    if 'A' in s:
        if s[:2] == '12':
            return '00' + s[2:-2]
        return s[:-2]
    elif s[:2] != '12':
        return str( int(s[:2]) + 12 ) + s[2:-2]
    return s[:-2]


print(timeConversion(fecha))
print(timeConversion(fecha2))
print(timeConversion(fecha3))
print(timeConversion(fecha4))