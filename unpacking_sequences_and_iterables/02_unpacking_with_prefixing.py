
print(divmod(20, 8))

t = (20,8)
print('Usar divmod con el prefijo *')
print(divmod(*t))

print('Unpacking with prefixing')
quotiet, reminder = divmod(*t)
print(quotiet, reminder)

print('Retornamos solo el valor que nos interesa')
import os
_, filename = os.path.split('/home/omar/.ssh/id_rsa.pub')
print(filename)