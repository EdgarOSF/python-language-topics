import re

email = input("What's your email? ").strip()

# p = r'^.+@.+\.edu$'
# p = r'^[^@]+@[^@]+\.edu$'
# p = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$'
p = r'^\w+@\w+\.edu$'

if re.search(p, email):
    print('Valid')
else:
    print('Invalid')