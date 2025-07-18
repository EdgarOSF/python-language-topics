class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('Name is missing')
        self.name = name


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house =  house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


albus = Wizard('Albus')
student = Student('Haryy', 'Gryffindor')
professor =  Professor('Severus', 'Defense Against the Dark Arts')