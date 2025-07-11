class Student:
    def __init__(self, name, house):
        self.name = name
        self.house =  house

    def __str__(self) -> str:
        return f'{self.name} from {self.house}'
    
    @classmethod
    def get(cls):
        name = input("What's your name: ")
        house = input("What's your house: ")

        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == '__main__':
    main()