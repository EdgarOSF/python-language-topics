def main():
    n = get_number()
    meow(n)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():

    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
    
main()