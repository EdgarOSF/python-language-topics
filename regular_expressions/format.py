import re


name = input("What's your username? ").strip()

# matches = re.search(r'^(.+), (.+)$', name)

# Version 1
# matches = re.search(r'^(.+), *(.+)$', name)
# if matches:
#     first, last = matches.groups()

# Version 2
if matches := re.search(r'^(.+), *(.+)$', name):
    name = matches.group(1) + ' ' + matches.group(2)
print(f'Hello, {name}')