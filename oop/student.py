class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError('Missing name')
        self.name = name
        self.house =  house

    def __str__(self) -> str:
        return f'{self.name} from {self._house}'
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
            raise ValueError('Invalid house')
        self._house =  house


def main():
    student = get_student()
    print(student)

def get_student():
    name =  input("What's your name: ")
    house =  input("What's your house: ")
    return Student(name, house)



if __name__ == '__main__':
    main()