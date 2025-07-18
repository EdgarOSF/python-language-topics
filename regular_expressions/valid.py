import re

email = input("What's your email? ").strip()

# p = r'^.+@.+\.edu$'
# p = r'^[^@]+@[^@]+\.edu$'
# p = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$'
# p = r'^\w+@\w+\.edu$'

p = r'^\w+@(\w+\.)?\w+\.edu$' # ?: puede aparecer 0 o 1 veces

if re.search(p, email, flags=re.IGNORECASE):
    print('Valid')
else:
    print('Invalid')