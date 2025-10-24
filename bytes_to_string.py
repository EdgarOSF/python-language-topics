# Method 1: Using decode method
byte_data = b'Hello, world!'
string_data = byte_data.decode('utf-8')
print(string_data)

# Method 2: Using the str() function
byte_data = b'Hello, world!'
string_data = str(byte_data, 'utf-8')
print(string_data)
